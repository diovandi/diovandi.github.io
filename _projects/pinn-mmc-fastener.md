---
title: PINN vs MMC Fastener Optimization
summary: A comparative research implementation for fastener-placement optimization across differentiable-physics and topology-based methods.
order: 8
year: 2025
category: Computational
organization: Independent research codebase
role: Developer and analyst
stack:
  - Python / PyTorch
  - Julia
  - Differentiable FEA
  - Topology optimization
repository: https://github.com/diovandi/pinn-mmc-fastener-optimization
---

This codebase compares two routes to fastener-placement optimization: a Physics-Informed Neural Network workflow built around differentiable finite-element kernels, and Moving Morphable Components topology optimization.

The implementation separates datasets, experiments, analysis tools, figures, CAD definitions, and thesis-style writing assets. Multi-geometry evaluation covers L-brackets, tapered plates, and ribbed channels under multiple loads, with utilities for unified comparisons, generalization tests, and Ansys-ready exports.

The current multi-geometry surrogate reports close agreement with differentiable FEA for the documented high-energy cases and sub-millisecond inference, but the repository also records its remaining work: larger datasets, external Ansys validation, and propagation of the latest evidence into the research narrative.

I include it as an **ongoing computational research implementation**, not as a completed or published thesis result. That status is part of the project: useful research software should make its unfinished validation boundary visible.
