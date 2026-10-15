---
title: "Stratos IV: live video and operational camera views"
summary: Networked camera endpoints, OBS production and remote fault recovery for DARE’s Stratos IV launch campaign, serving mission control, the pad crew and the public stream.
description: Networked camera endpoints, OBS production and remote fault recovery for DARE’s Stratos IV launch campaign, serving mission control, the pad crew and the public stream.
featured: true
order: 5
year: 2021–2022
date: 2026-07-24
category: Live production
organization: Delft Aerospace Rocket Engineering
role: Public Relations & Livestream Manager
stack:
  - Raspberry Pi OS Lite
  - SSH / systemd services
  - VLC / RTSP
  - OBS Studio
  - SPX-GC graphics
live_url: https://www.youtube.com/watch?v=GnA4juB8n3k
live_label: Watch the documentary
cover: /assets/images/photos/stratos-iv-rocket.webp
cover_width: 1600
cover_height: 1060
cover_alt: "Diovandi in a DARE team shirt standing behind the orange-nosed Stratos IV rocket on its transport cart at the launch site."
cover_caption: "With Stratos IV at the CEDEA range, Spain, during the 2021 launch campaign."
image: /assets/images/photos/stratos-iv-rocket.webp
---

Stratos IV was a student rocket built by Delft Aerospace Rocket Engineering (DARE). In September and October 2021 the team ran its launch campaign at INTA’s CEDEA range in Moguer, Spain. The rocket did not fly during that campaign, but the attempts still needed live camera views for the people running them and a public broadcast for supporters and sponsors.

## Context

The pad and the base were connected through the site’s existing fibre network, which INTA owned and managed. Mission control needed to see the tower, the umbilical and filling equipment, the pad and the nozzle area. The pad crew in the bunker and the crew viewing area needed views too. Once the flight termination system was installed, nobody was allowed back to the pad, so anything out there had to be recoverable remotely.

## My work

- Set up headless Raspberry Pi camera endpoints with webcams at the pad, the bunker, mission control and the crew area, running Raspberry Pi OS Lite with a service that started the stream after boot.
- Worked with INTA’s base IT lead and DARE’s electronics team to get the access and configuration the cameras needed on the site network.
- Brought the feeds into OBS on the production laptop, arranged them as a camera matrix, and sent views back to VLC displays in mission control and the crew area.
- Ran the public YouTube stream from the same setup, with a presenter camera and microphone, the team’s TeamSpeak communications and SPX-GC lower-third graphics.
- Connected processed telemetry from the electronics team to the graphics, and tested that data path with a simulated input. A teammate decoded the radio telemetry; the rocket did not fly, so the path was never used in flight.
- Trained members of the PR crew to repeat the setup for later launch attempts.

<div class="photo-pair screenshots">
  <figure>
    <img src="{{ '/assets/images/photos/stratos-iv-production-desk.webp' | relative_url }}" alt="The production desk seen from behind a crew member: a monitor shows the OBS camera matrix with bunker, filling-arm and pad views, next to a laptop running the team chat." width="1600" height="1067" loading="lazy" decoding="async">
  </figure>
  <figure>
    <img src="{{ '/assets/images/photos/stratos-iv-stream-operator.webp' | relative_url }}" alt="A crew member in a headset with a boom microphone working at a laptop, with OBS and the camera multiview on the monitors behind." width="1600" height="1067" loading="lazy" decoding="async">
  </figure>
</div>
<p class="photo-pair-caption">The production desk at the range: the OBS camera matrix with the bunker and filling-arm feeds, and the stream position with its headset and microphone.</p>

## The launch-attempt streams

These are the public livestreams from the campaign's launch attempts.

{% include youtube.html id="iK-Cbji4JR8" title="Stratos IV launch attempt livestream (1 of 3)" %}

{% include youtube.html id="f9pIYDG2Xpw" title="Stratos IV launch attempt livestream (2 of 3)" %}

{% include youtube.html id="vTfY-ceVEkU" title="Stratos IV launch attempt livestream (3 of 3)" %}

## A fault we had to solve

During the first dress rehearsal, camera feeds kept dropping out. We read the logs on the Pis over SSH and traced the problem to overheating in direct sunlight. Shading the Pis made the feeds stable again.

The dropouts also showed why remote recovery mattered. I could restart a stream service or reboot a Pi over SSH. For a Pi that stopped responding, a teammate proposed an Ethernet-connected Arduino and relay that could power-cycle it on command, which the team built into the setup.

## The wider campaign

Alongside the video work, I helped run the crowdfunding campaign that raised more than **€15,625**, standardised the visual and social-media guidelines, produced photo and video material, and delivered communications commitments for partners including Airbus, Arianespace, NLR and Teijin. The [Stratos IV crowdfunding page](https://www.supporttudelft.nl/project/stratosiv?locale=en) preserves the campaign and its result.

<figure>
  <img src="{{ '/assets/images/photos/stratos-iv-team.webp' | relative_url }}" alt="About fifty DARE team members in navy team shirts and face masks posing around the Stratos IV rocket in front of a hangar." width="1600" height="1067" loading="lazy" decoding="async">
  <figcaption>The Stratos IV launch campaign team, 2021.</figcaption>
</figure>

I was also the main videographer during the campaign; the [documentary case study](/projects/stratos-iv-documentary/) covers that work and who finished the film.

## Limits of this record

The network backbone and fibre link were INTA’s, not mine. The exact camera inventory and the mechanism that served the local RTSP views are not reconstructed here, so this page gives no camera count or network diagram.
