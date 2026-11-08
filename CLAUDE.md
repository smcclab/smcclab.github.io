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

- **Theme:** none. Layouts, includes and styles live in this repo: [Pico CSS](https://picocss.com) v2 vendored at `assets/vendor/pico/`, with the site's own overrides in `assets/css/main.css` (one accent colour, the orange from the lab logo, set as `--pico-primary` for light and dark mode). Same approach as the ACMA website.
- **Layouts:** `default` (head, nav, footer), `page` (set `hide_title: true` to drop the h1, `wide: true` for a 60rem column), `post`, `posts` (post list), `archive` (`type: years` or `type: tags`), `project`.
- **Plugins:** `jekyll-feed`, `jekyll-seo-tag`, `jekyll-sitemap`
- **Navigation:** Defined in `_data/navigation.yml` (keep it to one row; secondary pages such as Alumni, Archive and Tags are linked from the footer)
- **Homepage:** `index.md` is mostly HTML. The hero photo is picked at random on each visit from entries in `_data/performances.yml` that have an `images` list; the same entries feed the "On stage" grid and the performances page via `_includes/photo-grid.html`. Research areas are a `.cards` grid.

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

This writes `_projects/smcclab-<name>.md` there. Readers of the computing site see the project next to unrelated computing projects and don't know the lab's systems, so the exporter makes each page stand alone: it prepends an "About this project" section (a fixed paragraph about the lab and IMPSY, then the theme's `export_intro` if set, else its `intro`), links and glosses the first plain-text mention of lab terms (IMPSY, impsy-web, Bela Gem, MDRNN, course codes; see `TERMS` in the script) outside existing links and the background reading, adds the computing site's "How to Apply" section, and ends with a "More projects in the lab" section linking to smcclab.au/projects/. Write `export_intro` for a theme whenever its `intro` refers to sibling projects or assumes lab context. It warns if a cluster or group name is not a title in that repo's `_research/clusters` or `_research/groups`.

Computing-website vocabulary (must match exactly):

- `clusters`: always `Computing Foundations` only. Clusters are School of Computing subunits and Charles is in Foundations, so every lab project is a Foundations project regardless of topic.
- `groups`: `Human-Centred Computing` and `Sound, Music and Creative Computing Lab` (the "Lab" is part of the title there).
- `levels`: the computing site accepts only Bachelors, Honours, Masters, MPhil, PhD, Internship. `Short` is local to smcclab.au and means a six-week summer research scholarship or a one-semester 6-unit COMP3740 project (treated as equivalent); the exporter turns it into `Bachelors` plus a "Short project" line. All Honours and Master projects run over two semesters, so project bodies use **Short project:** / **Full project:** bullets, never semester counts.

### Includes

- `youtubePlayer.html` — responsive YouTube embed: `{% include youtubePlayer.html id="VIDEO_ID" %}`
- `mailing_list_form.html` — Mailchimp signup form
- `photo-grid.html` — grid of performance photos from `_data/performances.yml`: `{% include photo-grid.html limit=6 %}`

### Assets

Images go in `assets/` organized by year (e.g. `assets/2026/`). Reference with Liquid: `{% link assets/2026/image.jpg %}`. To put a performance photo on the homepage, add it to the `images` list of its entry in `_data/performances.yml`.

### Styling notes

- Markdown callout: `{:.info-box}` on a paragraph.
- Don't add gradients, shadows or hover transforms; Pico's defaults plus the accent colour are the whole design.
