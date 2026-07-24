---
title: Domestic Mobile Robot
summary: A complete ROS 2 navigation pipeline for a simulated service robot, from custom robot design and SLAM to Nav2 patrol analysis.
featured: true
order: 2
year: 2025
category: Robotics
organization: Swiss German University
role: Individual course project
stack:
  - ROS 2 Jazzy
  - Gazebo Harmonic
  - Nav2 / SLAM
  - Python
repository: https://github.com/diovandi/sgu-amr
---

I designed a custom differential-drive domestic robot and built the full autonomy stack around it: simulation, sensing, state estimation, mapping, localization, navigation, waypoint patrol, recording, and offline analysis.

The robot combines 2D LIDAR, an IMU, wheel odometry, Extended Kalman Filtering, SLAM Toolbox, AMCL, Nav2, and a modular ROS 2 launch architecture. The project progressed deliberately through six phases so each subsystem could be validated before integration.

## Engineering lessons

- A front caster-wheel change reduced false LIDAR detections—a reminder that mechanical design and perception cannot be debugged independently.
- Sensor QoS profiles and the `map → odom → base_link` transform hierarchy had to be made explicit before localization became stable.
- AMCL parameters and Nav2 lifecycle behavior were tuned for reliable autonomous patrol execution.
- Recorded patrol data was replayed to reconstruct trajectories and quantify tracking performance.

The final analysis measured a **0.15 m mean path deviation** over the recorded patrol and documented the remaining map–odom jitter under wheel-slip conditions. The public repository includes the ROS 2 workspace, robot description, environments, launch scripts, maps, patrol metadata, exercises, and report sources.
