---
title: "How much neural audio fits on a Bela Gem?"
tagline: "Benchmark which neural audio models can run in real time on the Bela Gem embedded platform."
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
  - neural-audio
  - embedded
  - Bela
  - benchmarking
theme: bela
order: 11
prerequisites: "Python and C++, some deep learning experience. Interest in audio signal processing."
---

Neural audio models such as neural amp models, differentiable DSP, and small autoencoders are becoming popular in music technology, but most need a laptop or GPU. Bela Gem's quad-core processor opens up new possibilities compared to the original Bela. In this project you'll benchmark which neural audio models can run in real time on Bela Gem, at what block sizes and sample rates, and what trade-offs you have to make in model size and quality. Useful starting points are [RTNeural](https://github.com/jatinchowdhury18/RTNeural) and the [pyBela/PyTorch cross-compilation tutorial](https://github.com/pelinski/pybela-pytorch-xc-tutorial) (written for the original Bela).

- **Short project:** one model family (e.g., LSTM amp models) with a benchmark harness covering model size, block size, and CPU load.
- **Full project:** more model families, a comparison with other embedded platforms, and a real-time neural audio effect or instrument.

## Background reading

- Martin, C. P., Jensenius, A. R. and Torresen, J. (2018). [Composing an Ensemble Standstill Work for Myo and Bela](https://charlesmartin.au/preprints/2018-ComposingEnsembleStandstillWork.pdf). *NIME 2018* (embedded Bela instruments in performance).
- Pelinski, T., Diaz, R., Benito Temprano, A. L. and McPherson, A. (2023). [Pipeline for recording datasets and running neural networks on the Bela embedded hardware platform](https://arxiv.org/abs/2306.11389). *NIME 2023*.
- Wright, A., Damskägg, E.-P., Juvela, L. and Välimäki, V. (2020). [Real-Time Guitar Amplifier Emulation with Deep Learning](https://doi.org/10.3390/app10030766). *Applied Sciences*.
- Chowdhury, J. (2021). [RTNeural: Fast Neural Inferencing for Real-Time Systems](https://arxiv.org/abs/2106.03037). *arXiv*.
