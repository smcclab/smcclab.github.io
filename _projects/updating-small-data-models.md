---
title: "Updating small-data music models across practice sessions"
tagline: "How should a musician's personal AI model be updated as they collect more data over weeks of practice?"
authors:
  - charles-martin
date: 2026-09-28
clusters:
  - Computing Foundations
groups:
  - Human-Centred Computing
  - Sound, Music and Creative Computing Lab
levels:
  - Summer
  - Honours
  - Masters
tags:
  - machine-learning
  - small-data
  - music
  - IMPSY
image: /assets/2026/projects/imps-pi-volca.jpg
image_alt: "A Raspberry Pi Zero running IMPSY, connected to a Korg Volca FM synthesiser and a power bank"
theme: living-with
order: 1
prerequisites: "Python and some machine learning (e.g., COMP3670 or COMP4670). Experience with Keras/TensorFlow is helpful."
---

IMPSY models are trained on tiny datasets: a few hours of one person's playing. In our recent experiments, a model trained on 7.4 hours of controller data from seven performances started to overfit after about 26 epochs. Musicians collect more data every time they play, so what's the best way to update a model? Retrain from scratch? Fine-tune the old model? How much new data does it take to change how the model behaves?

In this project you'll treat existing performance logs as a sequence of practice sessions, then compare strategies for updating an MDRNN after each one. A key part of the project is defining how to tell when a model has *actually* changed its musical behaviour, not just its validation loss (for example, by comparing the timing and values of gestures sampled from each model).

- **Summer or one semester:** a reproducible experiment pipeline using IMPSY's dataset tools; retraining vs. fine-tuning on one instrument's data; validation loss plus one behavioural measure.
- **Two semesters or Master:** add regularisation strategies and a second dataset (e.g., logs from the multi-week study project or other lab instruments), and recommend a procedure for updating models between sessions.

## Background reading

- Martin, C. P. and Torresen, J. (2019). [An Interactive Musical Prediction System with Mixture Density Recurrent Neural Networks](https://charlesmartin.au/preprints/2019-InteractiveMusicPredictionSystem.pdf). *NIME 2019* (the original IMPSY paper).
- Martin, C. P. (2024). [Generative AI for Musicians: Small-Data Prototyping to Design Intelligent Musical Instruments](https://generativeaiandhci.github.io/papers/2024/genaichi2024_50.pdf). *GenAICHI workshop, CHI 2024*.
- Fiebrink, R., Cook, P. R. and Trueman, D. (2011). [Human Model Evaluation in Interactive Supervised Learning](https://doi.org/10.1145/1978942.1978965). *CHI 2011* (evaluating models by how they behave, not just by accuracy).
