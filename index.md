---
layout: page
title: SMCClab
hide_title: true
wide: true
description: "The Sound, Music and Creative Computing Lab at the ANU School of Computing — building intelligent musical instruments that sense, understand, and perform."
tags: [SMCClab, ANU, sound, music, creative-computing, intelligent-instruments, research]
---

<section class="hero">
  <h1>New musical instruments that sense, understand, and perform.</h1>
  <p class="lead">We build intelligent instruments and creative computing systems at the Australian National University <a href="https://comp.anu.edu.au">School of Computing</a>, then take them on stage as both a research method and a creative output.</p>
  <p class="hero-actions">
    <a role="button" href="{{ '/performances/' | relative_url }}">See our performances</a>
    <a role="button" class="secondary outline" href="{{ '/join/' | relative_url }}">Join the lab</a>
  </p>
</section>

{%- assign shots = site.data.performances | where_exp: "p", "p.image" -%}
{%- assign first = shots | first %}
<figure class="hero-photo" id="hero-photo">
  <a href="{{ first.url | relative_url }}"><img src="{{ first.image | relative_url }}" alt="{{ first.image_alt }}"></a>
  <figcaption><a href="{{ first.url | relative_url }}">{{ first.title }}</a> &middot; {{ first.venue }}, {{ first.year }}</figcaption>
</figure>
<script type="application/json" id="hero-photos">[
{%- for p in shots %}
  {"src": {{ p.image | relative_url | jsonify }}, "alt": {{ p.image_alt | jsonify }}, "url": {{ p.url | relative_url | jsonify }}, "caption": {{ p.title | append: " · " | append: p.venue | append: ", " | append: p.year | jsonify }}}{% unless forloop.last %},{% endunless %}
{%- endfor %}
]</script>
<script>
// Show a different performance photo on each visit. Without JS, the newest one is shown.
(function () {
  var fig = document.getElementById('hero-photo');
  var data = document.getElementById('hero-photos');
  if (!fig || !data) return;
  var shots = JSON.parse(data.textContent);
  if (shots.length < 2) return;
  var pick = shots[Math.floor(Math.random() * shots.length)];
  var img = fig.querySelector('img'), links = fig.querySelectorAll('a'), cap = fig.querySelector('figcaption a');
  var pre = new Image();
  pre.onload = function () {
    img.src = pick.src; img.alt = pick.alt;
    links.forEach(function (a) { a.href = pick.url; });
    cap.textContent = pick.caption.split(' · ')[0];
    cap.nextSibling.textContent = ' · ' + pick.caption.split(' · ').slice(1).join(' · ');
  };
  pre.src = pick.src;
})();
</script>

Our lab develops **new musical instruments** that sense and understand music, actively **assisting musicians** during performances. We apply **computational intelligence**, **AR/VR**, and **sonic interaction design** in creative contexts, and explore how creative computing can inform studies of collaboration, spatial interaction, and decision making.

## Latest news

{% assign latest_post = site.posts | sort: 'date' | reverse | first %}
{% if latest_post %}
<h3><a href="{{ latest_post.url | relative_url }}">{{ latest_post.title }}</a></h3>
<p class="meta">{{ latest_post.date | date: "%-d %B %Y" }}</p>
{{ latest_post.excerpt }}
<p><a href="{{ latest_post.url | relative_url }}">Read more</a> &middot; <a href="{{ '/posts/' | relative_url }}">All posts and events</a></p>
{% endif %}

## Research areas

We apply research methods from human computer interaction, signal processing, and creative arts. In all of our work, creative interaction is used as a critical research method and as a medium for producing unique outputs.

<div class="cards">
  <div>
    <img src="{% link assets/collaboration.jpg %}" alt="Musicians playing networked touchscreen musical instruments together" loading="lazy">
    <h3>Collaborative interfaces</h3>
    <p>New ways for groups to make music together. Our <strong>touchscreen musical instruments</strong> communicate interactions over a network and engage performers in new kinds of <strong>ensemble interaction</strong>.</p>
  </div>
  <div>
    <img src="{% link assets/spatial.jpg %}" alt="Performer using freehand gestures with a spatial AR/VR musical instrument" loading="lazy">
    <h3>Spatial interaction</h3>
    <p><strong>Spatial musical apps</strong> for AR/VR computers. We experiment with new <strong>freehand gestures</strong> in AR and have deployed a spiral-shaped keyboard in collaborative music experiments and artistic performances.</p>
  </div>
  <div>
    <img src="{% link assets/spectrogram.jpg %}" alt="Spectrogram of AI-generated sound" loading="lazy">
    <h3>Generative sound</h3>
    <p>AI-generated sound could change the way we make music. We developed a <strong>singing-voice synthesis</strong> approach with more <strong>accurate duration predictions</strong>, and now work on <strong>text-to-sound</strong> generation models.</p>
  </div>
  <div>
    <img src="{% link assets/intelligent.jpg %}" alt="EMPI, a portable musical robot with a one-dimensional interface, responding to a performer" loading="lazy">
    <h3>Intelligent interfaces</h3>
    <p>Instruments that predict human musical interactions. We model <strong>embodied musical interactions</strong>, the movements of performers. Prototypes include <strong>EMPI</strong>, a portable musical robot with a 1-dimensional interface.</p>
  </div>
</div>

<div class="section-head">
  <h2 id="on-stage">On stage</h2>
  <a href="{{ '/performances/' | relative_url }}">All performances</a>
</div>

{% include photo-grid.html limit=6 %}

## Members

{% for person in site.data.lab-members %}
- [{{ person.name }}]({{ person.url }}) ({{ person.title }})
{% endfor %}

See also our [lab alumni and former students](/alumni/).

## Teaching

[Charles](https://charlesmartin.au) and other SMCClab members teach several courses at the ANU, including:

- [Sound and Music Computing (COMP4350/8350)](https://comp.anu.edu.au/courses/comp4350)
- [Human Computer Interaction (COMP3900/6390)](https://smcclab.au/thirty-nine-hundred-hci/)
- [Art and Interaction Computing (COMP1720/6720)](https://comp.anu.edu.au/courses/comp1720)
- [ANU Creative Computing Extension](https://comp.anu.edu.au/courses/extn1019/)

## Recent posts

<ul>
  {% for post in site.posts limit:6 %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> <span class="meta">({{ post.date | date: "%B %Y" }})</span></li>
  {% endfor %}
</ul>

[All posts and events](/posts/)

## Join our mailing list

{% include mailing_list_form.html %}
