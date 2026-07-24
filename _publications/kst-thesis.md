---
title: Implementation of Mechanical Assembly Rating Tool Based on Kinematic Screw Theory
summary: A bachelor’s thesis covering Python migration, CAD-connected data, higher-order constraints, verification, optimization, and interpretable outputs.
featured: true
order: 2
year: 2026
kind: Bachelor’s thesis
status: Defended and revised
venue: Swiss German University
authors: Diovandi Basheera Putra
repository: https://github.com/diovandi/kst-rating-tool
---

My thesis investigates how an assembly-rating method based on Kinematic Screw Theory can move from manually prepared research scripts into a reproducible engineering workflow.

The work reimplements the evaluator in Python, defines a versioned input contract, connects physical CAD selections through Fusion 360, verifies numerical parity against 21 reference cases, and studies bounded design revision using deterministic and stochastic search.

The analysis produces motion-resolved outputs rather than only a constrained/unconstrained label. That makes a weak rating traceable to the reciprocal motion and features responsible for it.

## Evidence included in the thesis

- Point, pin, line, and plane higher-order constraints
- MATLAB-to-Python benchmark comparisons
- JSON v2 CAD input and replay
- End-cap and printer-housing case studies
- Constant-interval and Differential Evolution searches
- Finite-difference and exploratory surrogate-model investigations
- Dashboard and report outputs intended for engineering interpretation

The public repository contains the maintained software and verification fixtures. The full academic working archive remains separate so unpublished drafts, private CAD binaries, and generated evidence are not mixed into the portfolio site.
