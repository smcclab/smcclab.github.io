---
title: "Scaling up wireless musical instrument networks"
tagline: "Measure how short-range radios behave in large networks of wireless musical instruments."
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
  - wireless
  - embedded
  - ESP32
  - networked-music
  - hardware
theme: hardware
order: 14
prerequisites: "Embedded programming (C/C++ on ESP32 or similar) and networking basics."
---

Our earlier work measured the latency and reliability of short-range radios (ESP-NOW, UWB, and 5GHz WiFi) for wireless musical instruments with up to four devices, and found that WiFi latency grew quickly as devices were added. Musical ensembles and installations often need many more devices than that. In this project you'll measure how these radios behave with 10 or more devices and different traffic patterns, and work out practical recommendations for wireless instrument designers.

- **Short project:** a measurement testbed and results for 10+ devices.
- **Full project:** optionally build a prototype wireless instrument and study how latency and packet loss affect performers in a group.

## Background reading

- Martin, C. P. (2023). [Composing Interface Connections for a Networked Touchscreen Ensemble](https://doi.org/10.1109/IEEECONF59510.2023.10335226). *ISIEA 2023*.
- Proctor, R. and Martin, C. P. (2020). [A Laptop Ensemble Performance System using Recurrent Neural Networks](https://charlesmartin.au/preprints/2020-NIME-LaptopEnsembleRNN.pdf). *NIME 2020*.
- Turchet, L., Fischione, C., Essl, G., Keller, D. and Barthet, M. (2018). [Internet of Musical Things: Vision and Challenges](https://doi.org/10.1109/ACCESS.2018.2872625). *IEEE Access*.
