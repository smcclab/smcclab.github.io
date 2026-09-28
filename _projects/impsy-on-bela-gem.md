---
title: "An intelligent instrument in one box: IMPSY on Bela Gem"
tagline: "Combine sensing, an AI model, and sound synthesis in one low-latency Bela Gem instrument."
authors:
  - charles-martin
date: 2026-09-28
clusters:
  - Computing Foundations
  - Intelligent Systems
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
theme: bela
order: 10
prerequisites: "C++ and some embedded or audio programming (e.g., COMP2300 or COMP4350/COMP8350). Some machine learning background is helpful."
---

IMPSY currently runs on a Raspberry Pi connected to external MIDI instruments. Bela Gem could combine sensing, the AI model, and sound synthesis in one low-latency device. IMPSY's models are small (two 64-unit LSTM layers and a mixture density output), so real-time inference on Bela Gem should be well within reach. In this project you'll write an MDRNN inference engine in C++ using weights exported from IMPSY's models, and verify it step by step against IMPSY's reference test vectors.

- **One semester:** a C++ MDRNN runtime that passes IMPSY's reference tests, plus latency and timing benchmarks against the Raspberry Pi version.
- **Two semesters or Master:** connect the model to Bela's sensor inputs and audio synthesis to build a playable standalone intelligent instrument, and evaluate it in performance.
