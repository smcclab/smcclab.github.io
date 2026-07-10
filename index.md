---
layout: page
title: SMCClab
---

<section class="home-hero" style="background-image: url('{% link assets/NIME2026-charles-yichen-performing-1.jpg %}');">
  <div class="home-hero-inner">
    <p class="home-hero-kicker">Sound, Music &amp; Creative Computing · ANU</p>
    <h2 class="home-hero-title">New musical instruments that sense, understand, and perform.</h2>
    <p class="home-hero-lead">We build intelligent instruments and creative computing systems — then take them on stage as both a research method and a creative output.</p>
    <p class="home-hero-actions">
      <a class="hero-btn hero-btn-primary" href="{{ '/performances/' | relative_url }}">See our performances</a>
      <a class="hero-btn" href="{{ '/join/' | relative_url }}">Join the lab</a>
    </p>
  </div>
</section>

Welcome to the Sound, Music, and Creative Computing Lab at the Australian National University [School of Computing](https://comp.anu.edu.au).

Our lab aims to develop **new musical instruments** that sense and understand music, actively **assisting musicians** during performances. We apply **computational intelligence**, **AR/VR**, and **sonic interaction design** in creative contexts. We explore how creative computing can inform studies of collaboration, spatial interaction, and decision making.

## Latest News

{% assign latest_post = site.posts | sort: 'date' | reverse | first %}

{% if latest_post %}
<article>
  <h3><a href="{{ latest_post.url | relative_url }}">{{ latest_post.title }}</a> ({{ latest_post.date | date: "%B %d, %Y" }})</h3>
  <p>{{ latest_post.excerpt }}</p>
  <a href="{{ latest_post.url | relative_url }}">Read more →</a>
</article>
{% endif %}

## Members

{% for person in site.data.lab-members %}
- [{{ person.name }}]({{ person.url }}) ({{ person.title }})
{% endfor %}

([list of lab alumni and former students](/alumni/))

SMCClab members are involved in teaching several courses at the ANU, including [Sound and Music Computing (COMP4350/8350)](https://comp.anu.edu.au/courses/comp4350), [Art and Interaction Computing (COMP1720/6720)](https://comp.anu.edu.au/courses/comp1720), [Human-Computer Interation (COMP3900/6390)](https://programsandcourses.anu.edu.au/course/comp3900) and [ANU Creative Computing Extension](https://comp.anu.edu.au/courses/extn1019/).

## Research Areas

SMCClab explores research in the broad area of sound, music and creative computing. We apply research methods from human computer interaction, signal processing, and creative arts. In all of our work, creative interaction is used as a critical research method and as a medium for producing unique outputs.

### Collaborative Interfaces

![Musicians playing networked touchscreen musical instruments together]({% link assets/collaboration.jpg %}){:.feature-img}

This research aims to create new ways for groups to make music together. We created **touchscreen musical instruments** that communicate interactions over a network.  These instruments engage music performers in new kinds of **ensemble interaction**.

### Spatial Interaction

![Performer using freehand gestures with a spatial AR/VR musical instrument]({% link assets/spatial.jpg %}){:.feature-img}

We create **authentic spatial musical apps** that support interaction in AR/VR computers. We experimented with new **freehand gestures** in AR and have deployed a spiral-shaped keyboard in collaborative music experiments as well as artistic performances.

### Generative Sound

![Spectrogram of AI-generated sound]({% link assets/spectrogram.jpg %}){:.feature-img}

AI-generated sound could change the way we make sounds and create music. We have developed a new approach to **singing-voice synthesis** focussed on more **accurate duration predictions**, enabling end-to-end training. We are now looking at novel **text-to-sound** generation models.

### Intelligent Interfaces

![EMPI, a portable musical robot with a one-dimensional interface, responding to a performer]({% link assets/intelligent.jpg %}){:.feature-img}

Intelligent instruments predict human musical interactions to help them create music. We model **embodied musical interactions**, or the movements of human performers. Our prototypes include **EMPI**, a portable musical robot that responds to performances with a 1-dimensional musical interface.

<section class="home-perf">
  <div class="home-perf-inner">
    <div class="home-perf-head">
      <h2>On stage</h2>
      <a href="{{ '/performances/' | relative_url }}">All performances →</a>
    </div>
    <div class="home-perf-scroll">
      <a href="{{ '/performances/' | relative_url }}"><img src="{% link assets/NIME2026-charles-yichen-performing-2.jpg %}" alt="Intelligent instrument performance at NIME 2026, London" loading="lazy"></a>
      <a href="{{ '/performances/' | relative_url }}"><img src="{% link assets/2026-charles-martin-soundout.jpg %}" alt="Charles Martin performing with intelligent instruments at SoundOut Festival 2026" loading="lazy"></a>
      <a href="{{ '/performances/' | relative_url }}"><img src="{% link assets/2025-smcclablive-1-1.jpg %}" alt="Spatial AR/VR musical performance at SMCClab Live" loading="lazy"></a>
      <a href="{{ '/performances/' | relative_url }}"><img src="{% link assets/2025-dream-tent.jpg %}" alt="Dream Tent installation with Martyn Jolly at the ANU Drill Hall Gallery" loading="lazy"></a>
      <a href="{{ '/performances/' | relative_url }}"><img src="{% link assets/2023-beyond-realms.jpg %}" alt="破境 // beyond realms by Yichen Wang and Sandy Ma at ACMC 2023" loading="lazy"></a>
      <a href="{{ '/performances/' | relative_url }}"><img src="{% link assets/metatone-hands-header.jpg %}" alt="Ensemble Metatone touchscreen performance" loading="lazy"></a>
      <a href="{{ '/performances/' | relative_url }}"><img src="{% link assets/2026-06-SandyMa-HautedTreasures-work.jpg %}" alt="Sandy Ma, Haunted Treasures at Platform, Canberra Contemporary" loading="lazy"></a>
    </div>
  </div>
</section>

## Teaching

![ANU Laptop Ensemble performing together]({% link assets/laptop-ensemble-promo.jpg %}){:.feature-img}

[Charles](https://charlesmartin.au) and other SMCClab members are involved in teaching several courses at the ANU, including:

- [Sound and Music Computing (COMP4350/8350)](https://comp.anu.edu.au/courses/laptop-ensemble), 
- [Human Computer Interaction (COMP3900/6390)](https://smcclab.github.io/thirty-nine-hundred-hci/),
- [Art and Interaction Computing (COMP1720/6720)](https://comp.anu.edu.au/courses/comp1720),
- [ANU Creative Computing Extension](https://comp.anu.edu.au/courses/extn1019/).

## Posts

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

## Join our Mailing List

{% include mailing_list_form.html %}
