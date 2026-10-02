---
title: "AI control voltages: an intelligent modular synthesiser voice"
tagline: "Bring intelligent instrument ideas to Eurorack modular synthesis with Bela Gem Multi."
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
  - modular-synthesis
  - hardware
  - Bela
  - intelligent-instruments
image: /assets/2026/projects/modular-synth-rig.jpg
image_alt: "A performance rig with a patched modular synthesiser, a Raspberry Pi running IMPSY, a Roland S-1 and MIDI controllers"
theme: bela
order: 12
prerequisites: "C++ and audio programming. Experience with modular synthesisers or analog electronics is very helpful."
---

Bela Gem Multi's DC-coupled outputs can send control voltages straight to a Eurorack modular synthesiser. In this project you'll build a system that learns gestures from a performer (from knobs, sensors, or incoming CV) and continues or responds to them as control voltages, bringing intelligent instrument ideas into modular synthesis. IMPSY's model can run on a Raspberry Pi that sends predictions to Bela Gem Multi for CV input and output, so this project doesn't depend on running models on the Bela itself.

- **Short project:** a working CV interface with IMPSY, and a demonstration with a modular synthesiser.
- **Full project:** interaction design for modular performers, evaluation in performance, and optionally a front panel or enclosure.

## Background reading

- Martin, C. P. et al. (2026). [Opening the Design Space: Two Years of Performance with Intelligent Musical Instruments](https://doi.org/10.5281/zenodo.20784072). *NIME 2026*.
- Martin, C. P. (2024). [Generative AI for Musicians: Small-Data Prototyping to Design Intelligent Musical Instruments](https://generativeaiandhci.github.io/papers/2024/genaichi2024_50.pdf). *GenAICHI workshop, CHI 2024*.
- McPherson, A. and Zappi, V. (2015). [An environment for submillisecond-latency audio and sensor processing on BeagleBone Black](https://www.aes.org/e-lib/browse.cfm?elib=17755). *AES Convention 138* (the original Bela paper).
