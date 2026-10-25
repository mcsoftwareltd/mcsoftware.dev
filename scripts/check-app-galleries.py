#!/usr/bin/env python3
"""Browser verification for the published app-gallery component.

Run against a locally built Jekyll site or the real site. Uses Playwright and
an explicitly supplied axe-core bundle; does not change the website or stores.
"""
import argparse
import json
import pathlib
from playwright.sync_api import sync_playwright


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-url', default='http://127.0.0.1:4000')
    parser.add_argument('--axe', required=True, type=pathlib.Path)
    parser.add_argument('--browser', help='Optional installed Chromium/Chrome executable')
    parser.add_argument('--report-dir', type=pathlib.Path)
    args = parser.parse_args()
    base = args.base_url.rstrip('/')
    assert args.axe.is_file(), 'Supply an existing axe.min.js bundle'
    errors = []
    report = {'viewports': [], 'accessibility': [], 'interactions': [], 'page_errors': errors}
    if args.report_dir:
        args.report_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=args.browser, headless=True, args=['--disable-gpu'])
        context = browser.new_context(reduced_motion='reduce', viewport={'width': 1440, 'height': 1100})
        page = context.new_page()
        page.on('pageerror', lambda error: errors.append(str(error)))
        for theme in ['light', 'dark']:
            page.emulate_media(color_scheme=theme)
            for width in [375, 390, 768, 1024, 1440]:
                page.set_viewport_size({'width': width, 'height': 1100})
                page.goto(base + '/', wait_until='networkidle')
                page.evaluate('document.fonts.ready')
                assert page.locator('.project-card').count() == 5
                assert page.locator('[data-gallery]').count() == 4
                assert not page.locator('.prototype-switcher, .app-stage-tabs, [data-variant-step]').count()
                assert page.evaluate('!document.documentElement.hasAttribute("data-variant")')
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), (theme, width)
                report['viewports'].append({'theme': theme, 'width': width, 'overflow': False})
                if width in [375, 1440]:
                    page.add_script_tag(path=str(args.axe))
                    audit = page.evaluate('''async () => {
                      const r = await axe.run(document, {runOnly: {type: 'tag', values: ['wcag2a','wcag2aa','wcag21a','wcag21aa']}});
                      return r.violations.map(v => ({id:v.id, impact:v.impact, nodes:v.nodes.map(n=>n.target)}));
                    }''')
                    report['accessibility'].append({'theme': theme, 'width': width, 'violations': audit})
                    assert not audit, json.dumps(audit)
                    if args.report_dir:
                        page.locator('#myvinyl').scroll_into_view_if_needed()
                        page.wait_for_function('document.querySelector("#myvinyl [data-rail=apple] img").complete')
                        page.locator('#myvinyl').screenshot(path=str(args.report_dir / f'gallery-{theme}-{width}.png'))

        page.emulate_media(color_scheme='light')
        page.set_viewport_size({'width': 375, 'height': 900})
        page.goto(base + '/', wait_until='networkidle')
        gallery = page.locator('[data-gallery][data-app="myvinyl"]')
        gallery.get_by_role('button', name='Android', exact=True).click()
        assert gallery.locator('[data-rail="android"]').is_visible()
        assert gallery.locator('[data-rail="android"] img').count() == 3
        assert 'play.google.com' in gallery.locator('.store-gallery__source a').get_attribute('href')
        gallery.get_by_role('button', name='Next My Vinyl screenshot', exact=True).click()
        page.wait_for_function('document.querySelector("#myvinyl [data-rail=android]").scrollLeft > 0')
        trigger = gallery.locator('[data-rail="android"] [data-lightbox]').nth(1)
        trigger.click()
        assert page.locator('dialog').is_visible()
        assert '/android/02.webp' in page.locator('dialog img').get_attribute('src')
        page.keyboard.press('ArrowRight')
        assert '/android/03.webp' in page.locator('dialog img').get_attribute('src')
        page.add_script_tag(path=str(args.axe))
        modal_audit = page.evaluate('''async () => (await axe.run(document, {runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa']}})).violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>n.target)}))''')
        assert not modal_audit, json.dumps(modal_audit)
        page.keyboard.press('Escape')
        page.wait_for_function('!document.querySelector("dialog").open && document.body.style.overflow === ""')
        assert trigger.evaluate('(el)=>el===document.activeElement'), 'Viewer must return focus to its trigger'
        gallery.get_by_role('button', name='iPhone', exact=True).click()
        assert gallery.locator('[data-rail="apple"]').is_visible()
        assert 'apps.apple.com' in gallery.locator('.store-gallery__source a').get_attribute('href')
        report['interactions'].extend(['platform switch and source URL', 'gallery arrow navigation', 'image viewer and keyboard next', 'modal accessibility', 'Escape and focus/scroll restoration'])

        expected = {'myvinyl': '1547173908', 'mapink': '6768144274', 'echoai': '6761034332', 'weekwise': '6759658981'}
        for slug, appid in expected.items():
            assert appid in page.locator(f'#{slug} .store-badge--apple').get_attribute('href')
        assert 'com.mcsoftware.myvinyl' in page.locator('#myvinyl .store-badge--google').get_attribute('href')
        assert not page.locator('#ridenav .store-badge').count()
        assert 'testflight.apple.com' in page.locator('#ridenav .beta-download').get_attribute('href')
        images = page.locator('.store-shot img').evaluate_all('(els)=>els.map(el=>el.getAttribute("src"))')
        assert len(set(images)) == 17
        for path in set(images + ['/assets/store/badges/app-store.svg', '/assets/store/badges/google-play.png']):
            assert context.request.get(base + path).status == 200, path
        for slug in ['echoai', 'mapink', 'weekwise', 'ridenav']:
            page.goto(base + '/' + slug + '/', wait_until='networkidle')
            assert page.locator('.store-downloads a').count() >= 1
            assert page.locator('[data-gallery]').count() == (0 if slug == 'ridenav' else 1)
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
        page.goto(base + '/echoai/privacy/', wait_until='networkidle')
        assert not page.locator('script[src*="app-galleries"], link[href*="app-galleries"]').count()
        report['interactions'].extend(['all download destinations', '17 distinct image HTTP checks', 'four product pages', 'legal pages unchanged'])

        nojs = browser.new_context(java_script_enabled=False)
        fallback = nojs.new_page()
        fallback.goto(base + '/', wait_until='networkidle')
        link = fallback.locator('#myvinyl [data-rail="apple"] .store-shot').first
        assert link.get_attribute('href').endswith('.webp')
        assert not fallback.locator('#myvinyl .gallery-arrow').first.is_visible()
        report['interactions'].append('no-JavaScript image links')
        nojs.close()
        browser.close()

    assert not errors, errors
    if args.report_dir:
        (args.report_dir / 'verification.json').write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
