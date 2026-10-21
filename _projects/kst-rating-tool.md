---
title: CAD-Integrated KST Assembly Rating Tool
summary: A verified Python and Fusion 360 workflow for analyzing how assembly features constrain rigid-body motion.
description: A verified Python and Fusion 360 workflow for analyzing how assembly features constrain rigid-body motion.
featured: true
order: 2
year: 2026
date: 2026-07-24
category: Research
area: ai-software
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
image: /assets/images/share/kst-fusion-wizard.jpg
---

This bachelor’s thesis turns a manually prepared MATLAB analysis into a reproducible CAD-to-analysis workflow. A Fusion 360 add-in captures point, pin, line, and plane constraints, exports them through a versioned JSON contract, and hands them to a deterministic Python evaluator.

The implementation reproduces Rusli’s higher-order-constraint method and reports motion-resolved assembly ratings such as Weakest Total Resistance, Mean Redundancy Ratio, Mean Total Resistance, and Trade-Off Ratio.

Leonard Rusli developed the analytical method and provided the original reference material. My work covered the Python implementation, Fusion integration, reference cases, optimization experiments and reports.

## Getting the geometry into the analysis

You select geometry in Fusion, the add-in writes an input file, and an external Python process runs the analysis and produces numerical and HTML reports. Having that file in between is useful because you can open it and see what was actually sent to the solver, and replay it outside Fusion. If a CAD example doesn’t match a reference case, the coordinates, directions, constraint types and units are there to compare.

<figure class="diagram">
  {% include diagrams/kst-pipeline.svg %}
  <figcaption>The versioned JSON file sits between Fusion 360 and the evaluator, so any analysis can be inspected and replayed from the command line.</figcaption>
</figure>

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

## Checking the numbers

The Python implementation was checked against MATLAB/Octave reference cases: 21 cases and four metrics, with an absolute tolerance of 0.001 and a relative tolerance of 5%.

The later manuscript review turned up a problem in the saved evidence: an old comparison CSV still contained superseded mismatch values. The comparison was rebuilt from saved solver outputs. For one end-cap case, the saved Python and Octave results used different constraint-model settings, so a matching Python branch was evaluated. The original files were kept, along with a note of which settings each one used.

So the package supports agreement across 21 comparable cases, combining saved outputs with that matching branch evaluation; both solvers weren’t rerun across the full set. It shows the implementation reproduces the reference calculations. Testing an actual assembly would be a separate step.

## How many times do you need to run the solver?

Every candidate arrangement in an optimization needs its own analysis. Constant Interval Search (CIS) checks a uniform grid: eleven points in each of two directions is 121 solver evaluations, and the count grows quickly with every extra variable.

The project compared finite differences, machine-learning surrogates and Differential Evolution (DE). For the surrogates there were two different questions: can a model learn the response of one assembly, and can it predict a new one? A model can fit a sampled case well and still transfer poorly. Training data has a cost too. If you need 121 solver calls to train a model for one assembly, you’ve already paid for the grid search before using the model.

DE became the selected method for the bounded line-search problem. It changes where it samples, while each candidate still goes through the same deterministic KST evaluator.

<figure class="diagram">
  {% include diagrams/kst-evaluations.svg %}
  <figcaption>Saved two-dimensional printer-housing run. Each evaluation is one call to the same KST evaluator. DE used fewer calls in exchange for a slightly lower rating.</figcaption>
</figure>

That comparison needed a correction as well. An earlier version used different evaluators for CIS and DE, which made CIS appear to fail. Once both used the same full objective, the result was more specific: DE got close to the grid result with fewer evaluations in the relevant two-dimensional cases. For a cheap one-dimensional case, CIS needed fewer evaluations.

The claim is deliberately narrow: this is an early-stage rigid-body constraint-layout method. It does not replace finite-element analysis or physical validation for stress, fatigue, preload loss, compliance, or joint failure.

## What I built

I led the Python reimplementation, CAD data contract, Fusion 360 integration, benchmark migration, optimization experiments, report generation, and reproducibility work. The maintained public repository contains the backend, add-in, fixtures, tests, and command-line tools without the private thesis working archive.

## Where AI came in

I used AI a lot at the beginning for code exploration and generation, and also for literature discovery, initial drafts and figures. Later I wrote and corrected more of the code myself, to understand it and to fix mistakes in the generated implementation. For the figures, I directed what I wanted to show, and I rewrote draft text in my own words.

There is substantial AI-written code in the project. The reference comparisons, saved inputs and reports are part of how that work was checked, and the manuscript, which is in preparation for submission, discloses the assistance.
