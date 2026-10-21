---
title: Domestic Mobile Robot
summary: A complete ROS 2 navigation pipeline for a simulated service robot, from custom robot design and SLAM to Nav2 patrol analysis.
description: A complete ROS 2 navigation pipeline for a simulated service robot, from custom robot design and SLAM to Nav2 patrol analysis.
featured: true
order: 3
year: 2025
date: 2026-07-24
category: Robotics
area: robotics-controls
organization: Swiss German University
role: Individual course project
stack:
  - ROS 2 Jazzy
  - Gazebo Harmonic
  - Nav2 / SLAM
  - Python
repository: https://github.com/diovandi/sgu-amr
cover: /assets/images/photos/amr-gazebo-rviz.webp
cover_width: 1600
cover_height: 573
cover_alt: "Gazebo showing the simulated house from above with the small blue robot inside, next to RViz showing the robot and its LIDAR scan points along nearby walls."
cover_caption: "The robot in the simulated house in Gazebo (left) and its LIDAR scan in RViz (right)."
image: /assets/images/share/amr-gazebo-rviz.jpg
---

I designed a custom differential-drive domestic robot and built the full autonomy stack around it: simulation, sensing, state estimation, mapping, localization, navigation, waypoint patrol, recording, and offline analysis.

The robot combines 2D LIDAR, an IMU, wheel odometry, Extended Kalman Filtering, SLAM Toolbox, AMCL, Nav2, and a modular ROS 2 launch architecture. The project progressed deliberately through six phases so each subsystem could be validated before integration.

## Engineering lessons

<figure>
  <img src="{{ '/assets/images/photos/amr-robot-model.webp' | relative_url }}" alt="The blue rudimentary_bot differential-drive model with grey wheels on a grey Gazebo floor, with a red box in the background." width="583" height="797" loading="lazy" decoding="async" style="max-width: 360px">
  <figcaption>The custom rudimentary_bot model in Gazebo.</figcaption>
</figure>

### A wall that wasn’t there

One issue was a false wall appearing in the map. When the simulated robot braked, its chassis pitched forward and the LiDAR hit the ground. Changing the sensor range could hide some of those detections, but the robot would still be pitching. Adding a front caster stabilized the chassis and dealt with the cause.

### One publisher per transform

The ROS components also had to agree on where the robot was. The EKF publishes `odom → base_link` and AMCL publishes `map → odom`. Each of those relationships needs exactly one publisher; otherwise every component can be running while giving conflicting descriptions of the robot’s position.

<figure class="diagram">
  {% include diagrams/amr-transforms.svg %}
  <figcaption>The localization transform chain and the node that owns each link.</figcaption>
</figure>

AMCL parameters and Nav2 lifecycle behaviour were then tuned for the waypoint patrol.

### Replaying the patrol

For the patrol analysis, I compared the planned path with filtered odometry transformed into the map frame. The frame and the playback clock had to line up for that comparison to mean anything.

Playback brought up a separate issue: the wheels appeared detached from the robot in RViz, because the recording didn’t include the dynamic joint states needed to display them. A separate robot description for analysis treats the wheel joints as fixed, so the robot can be shown with the data that exists. That fixed the display; it didn’t recover the missing wheel-motion measurements.

The final analysis measured a **0.15 m mean path deviation** over the recorded patrol and documented the remaining map–odom jitter under wheel-slip conditions. The public repository includes the ROS 2 workspace, robot description, environments, launch scripts, maps, patrol metadata, exercises, and report sources.

<figure>
  <img src="{{ '/assets/images/photos/amr-trajectory.webp' | relative_url }}" alt="X-Y plot in metres of the recorded patrol: the planned path in red and the actual path in blue follow each other closely, with jagged spikes in the planned path at turns and waypoints." width="1600" height="1000" loading="lazy" decoding="async">
  <figcaption>Planned (red) and actual (blue) robot position over the recorded patrol, in metres, plotted in PlotJuggler.</figcaption>
</figure>

## Checking against hardware

The project itself was built and analysed in simulation. Alongside it, we tested the software on an autonomous mobile robot available in SGU's lab, to check that what worked in Gazebo also held up on real hardware.

<div class="photo-pair">
  <figure>
    <img src="{{ '/assets/images/photos/amr-wiring.webp' | relative_url }}" alt="The SGU lab robot with its top frame open, showing batteries, a microcontroller board and wiring." width="472" height="629" loading="lazy" decoding="async">
    <figcaption>Inside the SGU lab robot.</figcaption>
  </figure>
  <figure>
    <img src="{{ '/assets/images/photos/amr-robot.webp' | relative_url }}" alt="The assembled SGU lab robot, a dark grey wheeled platform labelled Hybrid and Electric Vehicles, on a carpeted floor." width="388" height="441" loading="lazy" decoding="async">
    <figcaption>The assembled robot.</figcaption>
  </figure>
</div>
