---
layout: page
title: Performances
permalink: /performances/
description: "Concerts, installations and creative performances from the SMCClab at ANU — musical research with intelligent instruments, AR, and new interfaces, performed on stages around the world."
tags: [performances, concerts, music, creative-research, NIME, SMCClab, ANU]
---

Performance is central to how we do research. Playing music with intelligent
instruments — on stage, in galleries, and at festivals — is both a **research
method** (studying musical AI outside the lab) and a **creative output** in its
own right. Below is a record of concerts, installations, and productions
involving lab members. Lab members (current and former) are shown in **bold**.

<div class="perf-gallery">
  <img src="{% link assets/NIME2026-charles-yichen-performing-1.jpg %}" alt="Performing at NIME 2026, London" loading="lazy">
  <img src="{% link assets/2026-06-SandyMa-HautedTreasures-work.jpg %}" alt="Sandy Ma, Haunted Treasures at Platform, Canberra Contemporary" loading="lazy">
  <img src="{% link assets/NIME2026-charles-yichen-performing-2.jpg %}" alt="Intelligent instrument performance at NIME 2026" loading="lazy">
  <img src="{% link assets/2026-charles-martin-soundout.jpg %}" alt="Charles Martin performing with intelligent instruments at SoundOut Festival 2026" loading="lazy">
  <img src="{% link assets/2024-aicaif-concert.jpg %}" alt="AI Friends concert" loading="lazy">
  <img src="{% link assets/2025-smcclablive-1-1.jpg %}" alt="SMCClab Live concert" loading="lazy">
  <img src="{% link assets/2025-dream-tent.jpg %}" alt="Dream Tent installation with Martyn Jolly, ANU Drill Hall Gallery" loading="lazy">
  <img src="{% link assets/2023-beyond-realms.jpg %}" alt="破境 // beyond realms, Yichen Wang and Sandy Ma at ACMC 2023" loading="lazy">
  <img src="{% link assets/metatone-hands-header.jpg %}" alt="Ensemble Metatone touchscreen performance" loading="lazy">
  <img src="{% link assets/artificial-friends-min.jpg %}" alt="Artificial Friends performance" loading="lazy">
</div>

{% assign perfs_by_year = site.data.performances | group_by: "year" %}
{% for group in perfs_by_year %}
<h2 class="year-heading" id="perf-{{ group.name }}">{{ group.name }}</h2>
<ul class="entry-list">
  {% for perf in group.items %}
  <li class="entry">
    <span class="entry-kind">{{ perf.type }}</span>
    <span class="entry-body">
      {% if perf.url %}<a class="entry-title" href="{{ perf.url }}">{{ perf.title }}</a>{% else %}<span class="entry-title">{{ perf.title }}</span>{% endif %}
      <span class="entry-authors">{{ perf.authors }}</span>
      {% if perf.venue or perf.location %}
      <span class="entry-authors">{% if perf.venue %}{{ perf.venue }}{% endif %}{% if perf.venue and perf.location %} · {% endif %}{% if perf.location %}{{ perf.location }}{% endif %}</span>
      {% endif %}
      {% if perf.video %}
      <span class="entry-links"><a href="{{ perf.video }}">watch video</a></span>
      {% endif %}
    </span>
  </li>
  {% endfor %}
</ul>
{% endfor %}
