# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Site Overview

This is the Jekyll website for the Sound, Music and Creative Computing Lab (SMCClab) at ANU, deployed to GitHub Pages at smcclab.au.

## Commands

```bash
bundle exec jekyll serve    # local development server
bundle exec jekyll build    # production build
```

Requires Ruby 3.4.10 (see `.ruby-version`; the Gemfile adds `csv`, `base64` and `bigdecimal`, which Ruby 3.4 no longer bundles). Deployment is automated via GitHub Actions on push to `main`.

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

### Student projects

Projects are a Jekyll collection in `_projects/` (one file each, rendered at `/projects/<name>/` with `_layouts/project.html`). Front matter mirrors the ANU School of Computing website's `_projects` format (`title`, `tagline`, `authors`, `date`, `clusters`, `groups`, `levels`, `tags`) plus local keys: `theme` (a key in `_data/project_themes.yml`, which holds section titles and intros), `order`, `prerequisites`, optional `level_note`, and optional `image`/`image_alt` (a photo under `assets/2026/projects/`, shown on the project page and exported as an absolute smcclab.au URL). Each project ends with a `## Background reading` list of two to four papers: at least one lab paper and one external paper. `projects.md` is the grouped index.

To advertise a project on comp.anu.edu.au, export it into a local clone of `gitlab.anu.edu.au/jekyll-anu/computing-website`:

```bash
python3 scripts/export_to_computing.py ../computing-website <name> [<name>...]
```

This writes `_projects/smcclab-<name>.md` there, prepending the theme intro, adding the computing site's "How to Apply" section and linking back to smcclab.au. It warns if a cluster or group name is not a title in that repo's `_research/clusters` or `_research/groups`.

Computing-website vocabulary (must match exactly):

- `clusters`: always `Computing Foundations` only. Clusters are School of Computing subunits and Charles is in Foundations, so every lab project is a Foundations project regardless of topic.
- `groups`: `Human-Centred Computing` and `Sound, Music and Creative Computing Lab` (the "Lab" is part of the title there).
- `levels`: the computing site accepts only Bachelors, Honours, Masters, MPhil, PhD, Internship. `Short` is local to smcclab.au and means a six-week summer research scholarship or a one-semester 6-unit COMP3740 project (treated as equivalent); the exporter turns it into `Bachelors` plus a "Short project" line. All Honours and Master projects run over two semesters, so project bodies use **Short project:** / **Full project:** bullets, never semester counts.

### Includes

- `youtubePlayer.html` — responsive YouTube embed: `{% include youtubePlayer.html id="VIDEO_ID" %}`
- `mailing_list_form.html` — Mailchimp signup form
- `custom-head.html` — custom stylesheet link
- `footer.html` — lab logo footer

### Assets

Images go in `assets/` organized by year (e.g. `assets/2026/`). Reference with Liquid: `{% link assets/2026/image.jpg %}`.
