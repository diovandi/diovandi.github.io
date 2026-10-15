---
title: CAD-Integrated KST Assembly Rating Tool
summary: A verified Python and Fusion 360 workflow for analyzing how assembly features constrain rigid-body motion.
description: A verified Python and Fusion 360 workflow for analyzing how assembly features constrain rigid-body motion.
featured: true
order: 2
year: 2026
date: 2026-07-24
category: Research
organization: Swiss German University
role: Bachelor’s thesis · Lead developer and researcher
stack:
  - Python
  - NumPy / SciPy
  - Fusion 360
  - Optimization
repository: https://github.com/diovandi/kst-rating-tool
cover: /assets/images/photos/kst-fusion-wizard.webp
cover_width: 1600
cover_height: 1079
cover_alt: "Fusion 360 window with a printer-housing model and the KST Analysis Wizard panel listing line constraints, with buttons to add constraints, run the analysis and send a constraint to optimization."
cover_caption: "The KST Analysis Wizard add-in in Fusion 360, defining line constraints on the printer-housing example."
image: /assets/images/photos/kst-fusion-wizard.webp
---

This bachelor’s thesis turns a manually prepared MATLAB analysis into a reproducible CAD-to-analysis workflow. A Fusion 360 add-in captures point, pin, line, and plane constraints, exports them through a versioned JSON contract, and hands them to a deterministic Python evaluator.

The implementation reproduces Rusli’s higher-order-constraint method and reports motion-resolved assembly ratings such as Weakest Total Resistance, Mean Redundancy Ratio, Mean Total Resistance, and Trade-Off Ratio.

## Evidence and scope

- The Python workflow matched the MATLAB reference across **21 benchmark cases** within defined numerical tolerances.
- End-cap and printer-housing examples exercise the complete CAD extraction and replay path.
- Constant-interval search and Differential Evolution demonstrate bounded design revision on response surfaces that can be flat, piecewise smooth, or non-smooth.
- Intermediate JSON records, CLI runners, tests, and report outputs keep the analysis inspectable outside Fusion 360.

On the printer-housing example, 23 point, pin and line constraints captured in Fusion 360 give WTR 2.37, MRR 4.64, MTR 17.63 and TOR 3.80.

<div class="photo-pair screenshots">
  <figure>
    <img src="{{ '/assets/images/photos/kst-confirm.webp' | relative_url }}" alt="Confirm Constraints dialog listing the 23 printer-housing constraints with their locations and orientations in millimetres." width="481" height="974" loading="lazy" decoding="async">
    <figcaption>The constraints sent to the analysis.</figcaption>
  </figure>
  <figure>
    <img src="{{ '/assets/images/photos/kst-results.webp' | relative_url }}" alt="KST Analysis Wizard panel showing the constraint list and the results WTR 2.373, MRR 4.636, MTR 17.630 and TOR 3.802." width="764" height="1073" loading="lazy" decoding="async">
    <figcaption>The ratings returned in the wizard.</figcaption>
  </figure>
</div>

The claim is deliberately narrow: this is an early-stage rigid-body constraint-layout method. It does not replace finite-element analysis or physical validation for stress, fatigue, preload loss, compliance, or joint failure.

## What I built

I led the Python reimplementation, CAD data contract, Fusion 360 integration, benchmark migration, optimization experiments, report generation, and reproducibility work. The maintained public repository contains the backend, add-in, fixtures, tests, and command-line tools without the private thesis working archive.
