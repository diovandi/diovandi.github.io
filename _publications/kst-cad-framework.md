---
title: A CAD-Integrated Kinematic Screw Theory Framework for Feature-Level Assembly Constraint Analysis
summary: A reproducible CAD-to-KST method for early rigid-body constraint-layout assessment and bounded design revision.
featured: true
order: 1
year: 2026
kind: Research manuscript
status: Manuscript / preprint
venue: Swiss German University
authors: Leonard P. Rusli and Diovandi Basheera Putra
repository: https://github.com/diovandi/kst-rating-tool
---

This manuscript presents the research method developed around my bachelor’s thesis: selected CAD features are converted into an inspectable, versioned Kinematic Screw Theory record and evaluated by the same deterministic Python implementation used for verification.

## Main contributions

1. A CAD-to-KST contract for point, pin, line, circular-plane, and rectangular-plane constraints.
2. Feature-level higher-order constraints that preserve the analytical meaning of pins, lines, and planes.
3. A Python implementation matched against 21 MATLAB reference cases.
4. End-cap and printer-housing demonstrations of the complete CAD-assisted workflow.
5. Bounded design-revision experiments that retain exact KST evaluation on non-smooth response landscapes.

The paper separates evaluator verification from physical validation. Agreement with MATLAB shows that the implementation solves the intended numerical problem; it does not prove structural strength or predict fatigue, compliance, preload loss, or joint failure. That boundary is central to the research.

The manuscript is listed here by its current status and should not be read as a claim of peer-reviewed publication.
