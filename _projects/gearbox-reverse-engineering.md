---
title: WPA 50 Gearbox Reverse Engineering
summary: A documented teardown and reassembly of a 50:1 worm reducer, connecting component inspection to assembly sequence and serviceability.
description: A documented teardown and reassembly of a 50:1 worm reducer, connecting component inspection to assembly sequence and serviceability.
order: 10
year: 2026
date: 2026-07-24
category: Manufacturing
area: mechanical
organization: Politeknik Industri ATMI
role: Assembly & Reverse Engineering team project
stack:
  - Reverse engineering
  - Mechanical assembly
  - Technical documentation
  - Workshop practice
cover: /assets/images/photos/gearbox-layout.webp
cover_width: 900
cover_height: 1200
cover_alt: "The disassembled WPA 50 reducer laid out on cardboard: housing, worm shaft, output shaft, covers, bearings, sprockets, worm wheel, bolts and keys."
cover_caption: "The full teardown layout, before cleaning and reassembly."
image: /assets/images/photos/gearbox-layout.webp
---

As part of industrial training at ATMI, my teammate and I disassembled and reassembled a WPA 50 worm-gearbox reducer.

We documented the housing, covers, shafts, bearings, keys, sprockets, and 50-tooth worm wheel; recorded the practical order of operations; and connected those details to the power-transmission path. Removing external sprockets and bearings first reduced mechanical constraints and made the internal shafts accessible. During reassembly, correct key placement, bearing seating, and cover alignment were essential to restore smooth gear mesh.

<div class="photo-pair">
  <figure>
    <img src="{{ '/assets/images/photos/gearbox-worm-shaft.webp' | relative_url }}" alt="The worm shaft out of the housing, with an 11-tooth sprocket and a bearing still on it." width="750" height="1000" loading="lazy" decoding="async">
  </figure>
  <figure>
    <img src="{{ '/assets/images/photos/gearbox-output-shaft.webp' | relative_url }}" alt="The keyed output shaft laid out with two bearings, the 50-tooth worm wheel, a sprocket and the removed keys." width="750" height="1000" loading="lazy" decoding="async">
  </figure>
</div>
<p class="photo-pair-caption">Left: the worm shaft with its sprocket and bearing. Right: the output shaft, bearings, 50-tooth worm wheel and keys.</p>

## What the teardown made visible

- The 50:1 reduction comes from the worm and worm wheel; equal 11-tooth external sprockets do not change that internal ratio.
- Keys transfer torque between shafts, the wheel, and sprockets.
- Four bearings establish shaft position and support gear-mesh loads.
- Covers do more than close the housing: they retain bearings and preserve alignment and sealing surfaces.

The final report combines the procedure, component inventory, engineering observations, limitations, and photo evidence. It is a straightforward project, but a valuable reminder that system reliability often depends on small assembly details.
