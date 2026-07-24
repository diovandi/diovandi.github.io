---
title: CAD-Integrated KST Assembly Rating Tool
summary: A verified Python and Fusion 360 workflow for analyzing how assembly features constrain rigid-body motion.
featured: true
order: 1
year: 2026
category: Research
organization: Swiss German University
role: Bachelor’s thesis · Lead developer and researcher
stack:
  - Python
  - NumPy / SciPy
  - Fusion 360
  - Optimization
repository: https://github.com/diovandi/kst-rating-tool
---

This bachelor’s thesis turns a manually prepared MATLAB analysis into a reproducible CAD-to-analysis workflow. A Fusion 360 add-in captures point, pin, line, and plane constraints, exports them through a versioned JSON contract, and hands them to a deterministic Python evaluator.

The implementation reproduces Rusli’s higher-order-constraint method and reports motion-resolved assembly ratings such as Weakest Total Resistance, Mean Redundancy Ratio, Mean Total Resistance, and Trade-Off Ratio.

## Evidence and scope

- The Python workflow matched the MATLAB reference across **21 benchmark cases** within defined numerical tolerances.
- End-cap and printer-housing examples exercise the complete CAD extraction and replay path.
- Constant-interval search and Differential Evolution demonstrate bounded design revision on response surfaces that can be flat, piecewise smooth, or non-smooth.
- Intermediate JSON records, CLI runners, tests, and report outputs keep the analysis inspectable outside Fusion 360.

The claim is deliberately narrow: this is an early-stage rigid-body constraint-layout method. It does not replace finite-element analysis or physical validation for stress, fatigue, preload loss, compliance, or joint failure.

## What I built

I led the Python reimplementation, CAD data contract, Fusion 360 integration, benchmark migration, optimization experiments, report generation, and reproducibility work. The maintained public repository contains the backend, add-in, fixtures, tests, and command-line tools without the private thesis working archive.
