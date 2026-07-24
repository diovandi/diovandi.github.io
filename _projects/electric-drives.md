---
title: DC & AC Electric Drive Control
summary: Reproducible MATLAB/Simulink studies of DC motor control and induction-motor indirect field-oriented control.
order: 7
year: 2026
category: Controls
organization: Swiss German University
role: Individual course project
stack:
  - MATLAB
  - Simulink
  - Motor control
  - Python validation
repository: https://github.com/diovandi/electric-drives-2026
---

This project studies closed-loop speed and torque control for an armature-controlled DC motor and a three-phase squirrel-cage induction motor using indirect field-oriented control.

I built authoritative models in MATLAB R2025b and Simulink, with averaged converter and inverter stages because Simscape Electrical was unavailable in the working environment. A separate NumPy/SciPy implementation provides an independent numerical check for the DC response.

## Reproducible experiment set

Six cases cover no-load speed steps, load-torque disturbance rejection, and torque or current-command tracking for both machines. Each run exports time histories, plots, and metrics including rise time, settling time, overshoot, steady-state error, peak current, torque ripple, and recovery behavior.

The repository keeps model generation, simulation scripts, generated `.slx` files, CSV outputs, figures, and the LaTeX report together. One command rebuilds the models and evidence, making the report a reproducible engineering artifact rather than a collection of manually copied screenshots.
