---
title: DC & AC Electric Drive Control
summary: Reproducible MATLAB/Simulink studies of DC motor control and induction-motor indirect field-oriented control.
description: Reproducible MATLAB/Simulink studies of DC motor control and induction-motor indirect field-oriented control.
order: 7
year: 2026
date: 2026-07-24
category: Controls
organization: Swiss German University
role: Individual course project
stack:
  - MATLAB
  - Simulink
  - Motor control
  - Python validation
repository: https://github.com/diovandi/electric-drives-2026
cover: /assets/images/photos/drives-ac-speed-step.webp
cover_width: 1600
cover_height: 1206
cover_alt: "Simulation plots for the induction-motor speed step: speed rising to 1500 rpm with a small overshoot, electromagnetic torque, d- and q-axis currents, and voltage and flux."
cover_caption: "Induction motor under field-oriented control, no-load step to 1500 rpm: speed, torque, dq currents and voltage."
image: /assets/images/photos/drives-ac-speed-step.webp
---

This project studies closed-loop speed and torque control for an armature-controlled DC motor and a three-phase squirrel-cage induction motor using indirect field-oriented control.

I built authoritative models in MATLAB R2025b and Simulink, with averaged converter and inverter stages because Simscape Electrical was unavailable in the working environment. A separate NumPy/SciPy implementation provides an independent numerical check for the DC response.

## Reproducible experiment set

Six cases cover no-load speed steps, load-torque disturbance rejection, and torque or current-command tracking for both machines. Each run exports time histories, plots, and metrics including rise time, settling time, overshoot, steady-state error, peak current, torque ripple, and recovery behavior.

The repository keeps model generation, simulation scripts, generated `.slx` files, CSV outputs, figures, and the LaTeX report together. One command rebuilds the models and evidence, making the report a reproducible engineering artifact rather than a collection of manually copied screenshots.

## Results

| Case | Command | Rise (s) | Settling (s) | Overshoot | Peak current |
|---|---|---|---|---|---|
| DC speed step | 1500 rpm | 0.059 | 0.139 | 3.0% | 77.8 A |
| DC load step (8 N·m) | 1500 rpm | 0.059 | 0.808 | 3.0% | 77.8 A |
| Induction motor speed step | 1500 rpm | 0.343 | 1.05 | 12.7% | 14.6 A |
| Induction motor load step (9 N·m) | 1500 rpm | 0.343 | 1.43 | 12.7% | 14.6 A |

The DC drive reaches its current limit while accelerating, then backs off as the back EMF rises, and settles in 0.14 s with essentially no speed error. The induction motor is slower because the controller has to hold rotor flux while staying inside the inverter's voltage and current limits. In both load tests the speed returns to 1500 rpm with negligible error. The torque-tracking cases are judged from the plots rather than a single overshoot number, because each command has several levels and a reversal.

<figure>
  <img src="{{ '/assets/images/photos/drives-dc-speed-step.webp' | relative_url }}" alt="Simulation plots for the DC motor speed step: speed rising to 1500 rpm in about 0.1 s, a brief torque and current pulse at the current limit, and the converter voltage and duty cycle." width="1600" height="1154" loading="lazy" decoding="async">
  <figcaption>DC motor, no-load step to 1500 rpm: speed, torque, armature current and converter duty.</figcaption>
</figure>
