# MC Software ltd — Landing Page Design

**Date:** 2026-04-11
**Status:** Approved, build in progress

## Purpose

A GitHub Pages site at `mcsoftware.dev` that serves as the public face of MC Software ltd (small iOS studio) and the personal professional presence of Matteo Comisso. `mcomisso.me` will redirect here.

The site has a second job: hosting the EchoAI marketing page and its legally-required privacy policy and terms of service (EchoAI has no dedicated domain, unlike My Vinyl which lives at `myvinyls.app`).

## Positioning

**Hybrid.** Home page presents the studio and its apps. About page presents Matteo and the company. Equal weight — neither swallows the other.

## Site map

- `/` — home. Hero + inline project list. No separate `/projects` route.
- `/about` — Matteo + company + contact.
- `/echoai` — EchoAI marketing page.
- `/echoai/privacy` — EchoAI privacy policy.
- `/echoai/terms` — EchoAI terms of service.

My Vinyl is linked out to `myvinyls.app` from the home page project list. It does not have a dedicated page on this site.

## Tech stack

**Jekyll**, served natively by GitHub Pages. No GitHub Actions build pipeline. Custom domain `mcsoftware.dev` via `CNAME` file. Local dev: `bundle exec jekyll serve`. No Node, no npm, no Sass — single hand-written `assets/css/main.css`.

Adding a project = appending an entry to `_data/projects.yml` and dropping images into `assets/images/<slug>/`. No HTML edits required.

## File layout

```
LandingPage/
├── _config.yml
├── Gemfile
├── CNAME                          # mcsoftware.dev
├── _data/
│   └── projects.yml
├── _includes/
│   ├── head.html
│   ├── header.html
│   ├── footer.html
│   └── project_card.html
├── _layouts/
│   ├── default.html
│   ├── page.html
│   └── legal.html
├── assets/
│   ├── css/main.css
│   └── images/
│       ├── echoai/
│       └── myvinyl/
├── index.md
├── about.md
└── echoai/
    ├── index.md
    ├── privacy.md
    └── terms.md
```

## Visual system

**Direction:** Warm Paper (editorial / minimal-serif).

### Palette

```
--bg:          #FAF7F2   cream
--bg-elevated: #FFFFFF   pure white for images/cards on cream
--ink:         #1A1A1A   primary text
--ink-muted:   #5C5955   secondary text, meta
--rule:        #E8E2D6   hairlines
--accent:      #B2462D   terracotta — links, accents
--accent-ink:  #7A2E18   hover/active
```

Dark mode (via `prefers-color-scheme`):
```
--bg:     #151412
--ink:    #F0EBE0
--accent: #D76545
```

### Typography

- **Display** — Instrument Serif 400 (Google Fonts). H1/H2 only. Slight negative tracking.
- **Body** — Inter 400/500/600. 17px base, 1.6 line-height, max 65ch measure.
- **Meta labels** — Inter 12px uppercase, letter-spacing 0.08em. For "PROJECTS", "001 / ESTABLISHED 2024", etc.

Scale (1.25 ratio):
```
--fs-h1: 4.0rem      /* home hero */
--fs-h2: 2.6rem      /* section heads, project names */
--fs-h3: 1.5rem
--fs-body: 1.0625rem
--fs-meta: 0.75rem
```

### Layout

- Max width 68rem, 2rem side gutters.
- Prose blocks constrained to 38rem.
- Vertical section rhythm: 6rem desktop / 4rem mobile.
- Flexbox for nav, CSS Grid only for project-card image+text split.

### Motion

Near-none. `prefers-reduced-motion` respected. Subtle scroll fade-in is the ceiling.

### Accessibility

- Terracotta on cream: 5.8:1 (AA normal text).
- Ink on cream: 16.5:1 (AAA).
- All images have alt text via `projects.yml`.
- Focus rings: 2px terracotta outline, 2px offset.

## Page content

### `/` (home)

- Hero: `"Small studio. Native apps."` (Instrument Serif, 4rem). Subline: `"Built by Matteo Comisso."`
- Section label: `PROJECTS`
- Project list (stacked cards, one column): EchoAI, then My Vinyl.
- Footer: `© 2026 MC Software ltd · Registered in England and Wales · Company no. 16230837`

### `/about`

Long-form article, no sidebar. Section labels:
- `— / THE STUDIO`
- `— / THE DEVELOPER`
- `— / CONTACT`
- `— / COMPANY`

Contact email: `matteo@mcsoftware.dev`. GitHub: `@mcomisso`.

Prose is placeholder and gets replaced before publishing (city, bio, philosophy paragraphs).

### `/echoai` (marketing)

- Hero: large icon (128px), `EchoAI`, tagline `"On-device meeting intelligence."`
- App Store download badge (URL to be provided).
- Sections:
  - `WHAT IT DOES` — record, transcribe in real time, summarize, extract action items, semantic search.
  - `HOW YOUR DATA STAYS YOURS` — 100% on-device. Uses Apple Speech, WhisperKit, Foundation Models, SpeakerKit. No servers, no analytics, no account. Link to `/echoai/privacy`.
  - `REQUIREMENTS` — iOS 26+, Foundation Models requires Apple Intelligence–compatible hardware.
- Screenshots: 3 (recording view, session detail with transcript+summary, chat/search across sessions).

### `/echoai/privacy`

Verified against EchoAI source code (2026-04-11): no network code, no analytics, no third-party telemetry SDKs. Policy reflects reality.

Sections:
1. **What we collect** — Nothing. No MC Software backend exists.
2. **What the app stores on your device** — Audio recordings, transcripts, summaries, metadata. Sandboxed app storage. Included in iOS device backup per iOS defaults.
3. **Third-party services** — None. Speech + Foundation Models + WhisperKit + SpeakerKit all run locally.
4. **Permissions** — Microphone (recording), Speech Recognition (transcription). Grantable/revocable via iOS Settings.
5. **Children** — Not directed at children under 13.
6. **Changes** — Posted here with date.
7. **Contact** — matteo@mcsoftware.dev.

### `/echoai/terms`

Minimal indie-app EULA: as-is, no warranty, user owns their data, must comply with local recording laws, terms may be updated. Governed by laws of England and Wales.

## Open items (fill before publishing)

- [ ] City for hero subline ("Built in …")
- [ ] App Store URL for EchoAI download badge
- [ ] App Store URL for My Vinyl card (currently placeholder)
- [ ] Real bio copy on About page
- [ ] Headshot for About page (optional)
- [ ] Real EchoAI app icon + 3 screenshots in `assets/images/echoai/`
- [ ] Real My Vinyl app icon in `assets/images/myvinyl/`
- [ ] Registered office address on About page (if legally required to publish)
- [ ] Verify company registration country — assumed England and Wales based on 8-digit company number format (16230837)

## Build phases

1. **Scaffold** — Gemfile, `_config.yml`, CNAME, layouts, main.css. Empty pages render.
2. **Home + About** — copy in placeholder form, real structure.
3. **EchoAI marketing** — `/echoai/index.md` with sections.
4. **Privacy + Terms** — `/echoai/privacy.md` and `/echoai/terms.md`, verified against app source.
5. **Project data + cards** — `_data/projects.yml`, `project_card.html`, wire into home.

Each phase is independently viewable via `jekyll serve`.
