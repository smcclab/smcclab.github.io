---
layout: page
title: Student Projects
permalink: /projects/
description: "Honours, Master, summer research and COMP3740 projects available in the SMCClab at the ANU School of Computing: intelligent musical instruments, musical machine learning, Bela and embedded audio hardware."
tags: [honours, master, summer-research, COMP3740, projects, students, SMCClab, ANU, IMPSY, Bela]
---

These are projects available in the SMCClab for Honours and Master students, summer research scholars, and students taking a COMP3740 project course. Each one is a self-contained piece of work with its own report and artefact. Most of them also connect to a bigger research question in the lab, and good results can become part of a publication with the lab team.

If one of these interests you, read the [project expectations page](/honsproj/) and the [Join page](/join/), then get in touch with [Charles](https://comp.anu.edu.au/people/charles-martin/). Official listings are on the [ANU School of Computing project page](https://comp.anu.edu.au/study/projects/).

## How these projects work

- **Short projects** are either a six-week summer research scholarship (December to January) or a one-semester, 6-unit [COMP3740](https://programsandcourses.anu.edu.au/course/COMP3740) project. These are equivalent in scope and aim for one well-defined result.
- **Full projects** are Honours or Master research projects and run over two semesters.
- Projects marked *Short* list what the short version delivers and what the full project adds. Projects without a short version need a full two semesters.
- Lab hardware (Raspberry Pis, Bela boards, MIDI controllers) is provided for hardware projects.
- You'll join the weekly lab status meeting and book individual meetings when you need them (see [expectations](/honsproj/)).
- Your report is assessed on **your own work**. Where projects connect, each one has a fallback plan that doesn't depend on anyone else. Publications that combine results from several projects are a separate, optional output, and everyone who contributed is an author.

{% assign projects = site.projects | sort: "order" %}
{% for theme in site.data.project_themes %}
## {{ theme.title }}

{{ theme.intro }}

{% assign theme_projects = projects | where: "theme", theme.key %}
{% for p in theme_projects %}
- **[{{ p.title }}]({{ p.url | relative_url }})**  
  {{ p.tagline }} _({{ p.levels | join: ", " | replace: "Short", "Short (summer/COMP3740)" }})_
{% endfor %}
{% endfor %}
