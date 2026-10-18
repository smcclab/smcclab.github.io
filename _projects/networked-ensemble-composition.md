---
title: "Composing network connections for a touchscreen ensemble"
tagline: "Design new ways to compose with live network links between the instruments in an improvising ensemble."
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
  - networked-music
  - web
  - touchscreen
  - improvisation
  - composition
image: /assets/2026/projects/networked-touchscreen-ensemble.jpg
image_alt: "Four musicians in a studio playing networked touchscreen instruments, with cables and devices spread across the floor"
theme: hardware
order: 14
prerequisites: "Web development in JavaScript (the server is in Python). An interest in improvisation or ensemble performance; you don't need to be an expert musician."
---

In our networked touchscreen ensemble, each performer plays a web-based synthesiser on an iPad, and a server links controls between their instruments. When one performer turns a knob, the change can also appear on someone else's synth, possibly delayed or inverted. A composer writes a schedule of these *interface connections*, and the ensemble improvises within the changing set of links.

Our first sessions with this system found that the density of connections mattered more than which controls were linked. A single connection was rarely noticed, so we ended up copying rules until the composition file was 8000 lines long. The instrument also didn't show performers which of their controls were connected. In this project you'll take the next step: design a composition syntax built around connection density and types of connection, show performers what is connected to what, and test the new system in ensemble sessions.

- **Short project:** a compact composition syntax (e.g., "20 random connections, half of them delayed, for the next two minutes") and on-screen highlighting of linked controls, tested in sessions with the lab ensemble.
- **Full project:** the same, plus a performance study with outside musicians comparing composition techniques (e.g., direct, delayed, and inverted connections), which needs ethics approval. Another option is a composer agent that adjusts connections in response to what the ensemble is doing.

## Background reading

- Martin, C. P., Hunter, A., Schuetze, B. and Wang, Y. (2023). [Composing Interface Connections for a Networked Touchscreen Ensemble](https://doi.org/10.1109/IEEECONF59510.2023.10335226). *IEEE International Symposium on the Internet of Sounds (IS² 2023)*. [Preprint](https://charlesmartin.au/preprints/2023-composing-interface-connections.pdf).
- Martin, C., Gardner, H., Swift, B. and Martin, M. (2016). [Intelligent Agents and Networked Buttons Improve Free-Improvised Ensemble Music-Making on Touch-Screens](https://doi.org/10.1145/2858036.2858269). *CHI 2016*.
- Weinberg, G. (2005). [Interconnected Musical Networks: Toward a Theoretical Framework](https://doi.org/10.1162/0148926054094350). *Computer Music Journal*.
