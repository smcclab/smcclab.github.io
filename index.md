---
layout: page
title: SMCClab
---

Welcome to the Sound, Music, and Creative Computing Lab at the Australian National University [School of Computing](https://comp.anu.edu.au).
![]({% link assets/smcclab-title-slide.jpg %})

Our lab aims to develop **new musical instruments** that sense and understand music, actively **assisting musicians** during performances. We apply **computational intelligence**, **AR/VR**, and **sonic interaction design** in creative contexts. We explore how creative computing can inform studies of collaboration, spatial interaction, and decision making.

Members of the SMCClab are:

- [Dr Charles Martin](https://charlesmartin.au) (**lead researcher**).
- [Minsik Choi](https://yorkcla.github.io) (PhD researcher)
- [Xinlei Niu](https://www.linkedin.com/in/xinlei-niu-544ab6216/) (PhD researcher)
- [Yichen Wang](https://yichenwangs.github.io) (PhD researcher)
- [Sandy Ma](https://snud.me) (Phd researcher)

SMCClab members are involved in teaching several courses at the ANU, including [Sound and Music Computing (COMP4350/8350)](https://comp.anu.edu.au/courses/comp4350), [Art and Interaction Computing (COMP1720/6720)](https://comp.anu.edu.au/courses/comp1720), [Human-Computer Interation (COMP3900/6390)](https://programsandcourses.anu.edu.au/course/comp3900) and [ANU Creative Computing Extension](https://comp.anu.edu.au/courses/extn1019/).

# Research Areas

## Collaborative Interfaces

![]({% link assets/collaboration.jpg %})

This research aims to create new ways for groups to make music together. We created **touchscreen musical instruments** that communicate interactions over a network.  These instruments engage music performers in new kinds of **ensemble interaction**. 

## Spatial Interaction

![]({% link assets/spatial.jpg %})

We create **authentic spatial musical apps** that support interaction in AR/VR computers. We experimented with new **freehand gestures** in AR and have deployed a spiral-shaped keyboard in collaborative music experiments as well as artistic performances.

## Generative Sound

![]({% link assets/spectrogram.jpg %})

AI-generated sound could change the way we make sounds and create music. We have developed a new approach to **singing-voice synthesis** focussed on more **accurate duration predictions**, enabling end-to-end training. We are now looking at novel **text-to-sound** generation models.

## Intelligent Interfaces

![]({% link assets/intelligent.jpg %})

Intelligent instruments predict human musical interactions to help them create music. We model **embodied musical interactions**, or the movements of human performers. Our prototypes include **EMPI**, a portable musical robot that responds to performances with a 1-dimensional musical interface.

# Teaching

![]({% link assets/laptop-ensemble-promo.jpg %})

[Charles](https://charlesmartin.au) and other SMCClab members are involved in teaching several courses at the ANU, including [Sound and Music Computing (COMP4350/8350)](https://comp.anu.edu.au/courses/laptop-ensemble), [Art and Interaction Computing (COMP1720/6720)](https://comp.anu.edu.au/courses/comp1720) and [ANU Creative Computing Extension](https://comp.anu.edu.au/courses/extn1019/).

# Posts

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

# Join our Mailing List

{% include mailing_list_form.html %}
