---
title: "An intelligent instrument in one box: IMPSY on Bela Gem"
tagline: "Combine sensing, an AI model, and sound synthesis in one low-latency Bela Gem instrument."
authors:
  - charles-martin
date: 2026-09-28
clusters:
  - Computing Foundations
groups:
  - Human-Centred Computing
  - Sound, Music and Creative Computing Lab
levels:
  - Honours
  - Masters
tags:
  - embedded
  - Bela
  - C++
  - real-time
  - IMPSY
image: /assets/2026/projects/bela-myo-headphones.jpg
image_alt: "A Bela embedded computer on a desk between a Myo armband and a pair of headphones"
theme: bela
order: 10
prerequisites: "C++ and some embedded or audio programming (e.g., COMP2300 or COMP4350/COMP8350). Some machine learning background is helpful."
---

IMPSY currently runs on a Raspberry Pi connected to external MIDI instruments. Bela Gem could combine sensing, the AI model, and sound synthesis in one low-latency device. IMPSY's models are small (two 64-unit LSTM layers and a mixture density output), so real-time inference on Bela Gem should be well within reach. In this project you'll write an MDRNN inference engine in C++ using weights exported from IMPSY's models, and verify it step by step against IMPSY's reference test vectors.

- **One semester:** a C++ MDRNN runtime that passes IMPSY's reference tests, plus latency and timing benchmarks against the Raspberry Pi version.
- **Two semesters or Master:** connect the model to Bela's sensor inputs and audio synthesis to build a playable standalone intelligent instrument, and evaluate it in performance.

## Background reading

- Martin, C. P. and Torresen, J. (2019). [An Interactive Musical Prediction System with Mixture Density Recurrent Neural Networks](https://charlesmartin.au/preprints/2019-InteractiveMusicPredictionSystem.pdf). *NIME 2019* (the original IMPSY paper).
- Martin, C. P., Jensenius, A. R. and Torresen, J. (2018). [Composing an Ensemble Standstill Work for Myo and Bela](https://charlesmartin.au/preprints/2018-ComposingEnsembleStandstillWork.pdf). *NIME 2018* (embedded Bela instruments in performance).
- Pelinski, T., Diaz, R., Benito Temprano, A. L. and McPherson, A. (2023). [Pipeline for recording datasets and running neural networks on the Bela embedded hardware platform](https://arxiv.org/abs/2306.11389). *NIME 2023*.
