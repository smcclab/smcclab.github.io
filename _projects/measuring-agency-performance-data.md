---
title: "Who's leading? Measuring agency in human-AI performance data"
tagline: "Can information-theoretic measures detect who is leading in human-AI musical performance?"
authors:
  - charles-martin
date: 2026-09-28
clusters:
  - Computing Foundations
groups:
  - Human-Centred Computing
  - Sound, Music and Creative Computing Lab
levels:
  - Short
  - Honours
  - Masters
tags:
  - theory
  - information-theory
  - data-analysis
  - agency
  - IMPSY
image: /assets/2026/projects/duet-patch-latent-viz.jpg
image_alt: "A Pure Data patch with a latent-space visualisation and a video feed of two performers on stage"
theme: theory
order: 8
prerequisites: "Strong mathematics or statistics (e.g., probability and information theory) and Python."
---

When a musician plays with an intelligent instrument, who is leading? Our qualitative work suggests that the answer shifts from moment to moment. In this project you'll test whether quantitative measures such as transfer entropy or Granger causality can detect these shifts in logs of human and AI gestures from IMPSY performances. You'll start with synthetic data, where the right answer is known, and then apply the measures to real performance data. Most existing IMPSY logs record only the human side, so you'll record new sessions with AI prediction logging turned on (we'll help), across IMPSY's interaction modes. Modes where the human and AI play at the same time are the most interesting, because in call-and-response mode the turn-taking is fixed by design.

- **Short project:** a validated analysis toolkit, tested on synthetic call-and-response data and applied to one set of performance logs.
- **Full project:** a comparison between quantitative measures and qualitative accounts of the same performances (your own reflections, or interviews with other performers, which need ethics approval), and a discussion of what each approach can and can't capture.

## Background reading

- Wang, Y. and Martin, C. P. (2026). [回溯: Co-constructing a Dual Feedback Apparatus](https://doi.org/10.5281/zenodo.20782069). *NIME 2026* (music paper on our AI feedback duet and material agency).
- Martin, C. P., Gardner, H. and Swift, B. (2015). [Tracking Ensemble Performance on Touch-Screens with Gesture Classification and Transition Matrices](https://charlesmartin.au/preprints/2015-NIME-TrackingEnsemblePerformance.pdf). *NIME 2015* (quantitative analysis of performance logs).
- Schreiber, T. (2000). [Measuring Information Transfer](https://doi.org/10.1103/PhysRevLett.85.461). *Physical Review Letters* (transfer entropy).
