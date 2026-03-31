# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Site Overview

This is the Jekyll website for the Sound, Music and Creative Computing Lab (SMCClab) at ANU, deployed to GitHub Pages at smcclab.au.

## Commands

```bash
bundle exec jekyll serve    # local development server
bundle exec jekyll build    # production build
```

Requires Ruby 3.2.2 (see `.ruby-version`). Deployment is automated via GitHub Actions on push to `main`.

## Architecture

- **Theme:** Custom `monophase` theme (loaded from git, `https://github.com/cpmpercussion/monophase.git`)
- **Plugins:** `jekyll-feed`, `jekyll-paginate`, `jekyll-seo-tag` (via theme)
- **Navigation:** Defined in `_data/navigation.yml`

### Content structure

**Posts** live in `_posts/` with the filename convention `YYYY-MM-DD-slug.md` and front matter:
```yaml
---
layout: post
title: "Title"
date: YYYY-MM-DD
description: "Short description for SEO"
tags: [tag1, tag2]
---
```

**Root pages:** `index.md`, `about.md`, `join.md`, `posts.md`, `tags.md`

### Includes

- `youtubePlayer.html` — responsive YouTube embed: `{% include youtubePlayer.html id="VIDEO_ID" %}`
- `mailing_list_form.html` — Mailchimp signup form
- `custom-head.html` — custom stylesheet link
- `footer.html` — lab logo footer

### Assets

Images go in `assets/` organized by year (e.g. `assets/2026/`). Reference with Liquid: `{% link assets/2026/image.jpg %}`.
