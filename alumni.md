---
layout: page
title: Lab Alumni
permalink: /alumni/
description: "Research output and profiles of PhD, master and honours students who have graduated from the SMCClab at ANU."
tags: [alumni, students, research, SMCClab, graduates]
---

Here are links to research produced by PhD, Master, and Honours students who have studied in the SMCClab.

If you'd like to work on something like this, check out the details on our [join page](/join/).

{% for person in site.data.lab-alumni %}
#### {% if person.url %}[{{ person.name }}]({{ person.url }}){% else %}{{ person.name }}{% endif %} ({{ person.title }} {{ person.dates }})

{{ person.project-title }} {% if person.thesis-url %}[(thesis)]({{ person.thesis-url }}){% endif %}{% if person.publication %} [(paper)]({{ person.publication }}){% endif %}

{{ person.note }}

{% endfor %}
