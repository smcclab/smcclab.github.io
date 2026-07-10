---
layout: page
title: Publications
permalink: /publications/
description: "Peer-reviewed publications from the Sound, Music and Creative Computing Lab (SMCClab) at ANU — papers at NIME, CHI, ICASSP, ICML, AAAI, C&C and more."
tags: [publications, research, papers, NIME, CHI, SMCClab, ANU]
---

Research from the SMCClab appears at leading venues across computer music, machine
learning, and human–computer interaction — including
**NIME**, **CHI**, **ICASSP**, **Interspeech**, **ICML**, **AAAI**, and
**Creativity & Cognition**. Lab members (current and former) are shown in **bold**.

{% assign pubs_by_year = site.data.publications | group_by: "year" %}
{% for group in pubs_by_year %}
<h2 class="year-heading" id="pubs-{{ group.name }}">{{ group.name }}</h2>
<ul class="entry-list">
  {% for pub in group.items %}
  <li class="entry">
    <span class="entry-venue{% if pub.top %} is-top{% endif %}">{{ pub.venue }}</span>
    <span class="entry-body">
      {% if pub.url %}<a class="entry-title" href="{{ pub.url }}">{{ pub.title }}</a>{% else %}<span class="entry-title">{{ pub.title }}</span>{% endif %}
      <span class="entry-authors">{{ pub.authors }}</span>
      {% if pub.preprint or pub.video %}
      <span class="entry-links">
        {% if pub.preprint %}<a href="{{ pub.preprint }}">preprint</a>{% endif %}
        {% if pub.video %}<a href="{{ pub.video }}">video</a>{% endif %}
      </span>
      {% endif %}
    </span>
  </li>
  {% endfor %}
</ul>
{% endfor %}

<p class="list-intro" style="margin-top:2em;font-size:0.85em;color:#666;">
This list is generated from our
<a href="https://github.com/cpmpercussion/preprints/blob/main/publications.bib">public BibTeX record</a>.
A fuller record including creative works, software, and talks is on
<a href="https://charlesmartin.au">Charles Martin's site</a> and
<a href="https://scholar.google.com/citations?user=fF9nUQ8AAAAJ">Google Scholar</a>.
</p>
