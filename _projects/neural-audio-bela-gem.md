---
title: "How much neural audio fits on a Bela Gem?"
tagline: "Benchmark which neural audio models can run in real time on the Bela Gem embedded platform."
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
  - Summer
  - Honours
  - Masters
tags:
  - neural-audio
  - embedded
  - Bela
  - benchmarking
theme: bela
order: 11
prerequisites: "Python and C++, some deep learning experience. Interest in audio signal processing."
---

Neural audio models such as neural amp models, differentiable DSP, and small autoencoders are becoming popular in music technology, but most need a laptop or GPU. Bela Gem's quad-core processor opens up new possibilities compared to the original Bela. In this project you'll benchmark which neural audio models can run in real time on Bela Gem, at what block sizes and sample rates, and what trade-offs you have to make in model size and quality. Useful starting points are [RTNeural](https://github.com/jatinchowdhury18/RTNeural) and the [pyBela/PyTorch cross-compilation tutorial](https://github.com/pelinski/pybela-pytorch-xc-tutorial) (written for the original Bela).

- **Summer or one semester:** one model family (e.g., LSTM amp models) with a benchmark harness covering model size, block size, and CPU load.
- **Two semesters or Master:** more model families, a comparison with other embedded platforms, and a real-time neural audio effect or instrument.
