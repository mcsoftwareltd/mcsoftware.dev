# mcsoftware.dev

Landing page for MC Software ltd. Built with Jekyll, hosted on GitHub Pages.

## Local development

```sh
bundle install
bundle exec jekyll serve
```

Site runs at http://localhost:4000.

## Adding a project

1. Add an entry to `_data/projects.yml`.
2. Drop the app icon into `assets/images/<slug>/`.
3. Add genuine store screenshots under `assets/store/<slug>/` and their dimensions, alt text and original URLs to `_data/store_media.json`.
4. The home page picks up the app and its screenshot shelf automatically. See [the gallery component guide](docs/app-galleries.md) for product-page usage and verification.

## Editing legal pages

EchoAI privacy/terms live at `echoai/privacy.md` and `echoai/terms.md`. Edit the Markdown directly.

## Deploying

Push to `main`. GitHub Pages builds automatically.
