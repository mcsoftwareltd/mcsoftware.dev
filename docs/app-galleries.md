# App screenshot shelves

The portfolio uses the approved **Store shelves (A)** layout: app identity, description and official download badges above a horizontally swipeable screenshot rail. Other prototype layouts and the prototype switcher are not part of production. The original comparison remains on the local `prototype/store-screenshots` branch.

## Data and includes

- `_data/projects.yml` owns app names, copy, icons and exact store URLs.
- `_data/store_media.json` owns platform labels, screenshot source URLs, local image paths, dimensions and alt text. Its `_sources` entry records first-party badge provenance.
- `assets/store/<slug>/` contains the saved, proportionally optimized store screenshots. Do not replace unavailable screenshots with invented UI or another app's images.
- `{% raw %}{% include store_badges.html project=project %}{% endraw %}` renders official App Store/Google Play artwork only for actual published links. A TestFlight URL renders a separate beta action.
- `{% raw %}{% include app_screenshots.html slug="mapink" context="product" %}{% endraw %}` renders a gallery if real images exist. `context` plus `slug` makes rail IDs unique when rendering more than one instance on the same page.
- Set `store_gallery: true` in page frontmatter to load gallery styling, behavior and the shared image viewer. Legal and unrelated pages do not load them.

The home page has galleries for My Vinyl, MapInk, EchoAI and Weekwise. My Vinyl also has a separate Android rail. RideNav remains a TestFlight-only action because no public screenshot gallery was available; FarmacoCalendar remains an unlisted coming-soon page.

## Interaction and accessibility

Screenshots retain their original aspect ratios and full compositions, including any device frames already present in the store artwork. The rail supports touch/trackpad scrolling, scroll snapping, previous/next buttons and arrow keys when the rail itself has focus. Platform buttons expose their selected state and control the matching rail. Their provenance link changes with the selected platform.

Screenshot links open the original image without JavaScript. With supported native `<dialog>` behavior, they instead open a full-screen viewer with previous/next, arrow keys, Escape/Close, an original-image link and a loading/error message. Native dialog focus trapping is retained; close restores focus and scrolling. Modified link clicks retain normal browser behavior. Reduced-motion preferences disable animated scrolling. There is no tracking, persistence or store-side mutation.

## Verification

Build the site using the existing Gemfile:

```sh
JEKYLL_ENV=production bundle exec jekyll build
bundle exec jekyll serve
```

For browser checks, install Playwright into a development-only environment, obtain the official `axe-core` npm package (the initial audit used 4.14.0), and supply its `axe.min.js` to:

```sh
uv run --with playwright python scripts/check-app-galleries.py \
  --base-url http://127.0.0.1:4000 \
  --axe /path/to/axe.min.js \
  --browser /path/to/chrome \
  --report-dir /path/to/verification-output
```

Omit `--browser` to use Playwright's installed Chromium. No test code is shipped by Jekyll: `scripts/`, `docs/` and `AGENTS.md` are excluded from output.

The check covers five viewport widths in light/dark mode, automated WCAG 2/2.1 A/AA checks at mobile and desktop widths and inside the viewer, platform switching, screenshot navigation, focus/scroll restoration, all download targets, every saved image, product-page galleries and the no-JavaScript fallback. It also checks that no prototype selector or alternate-layout logic is rendered.
