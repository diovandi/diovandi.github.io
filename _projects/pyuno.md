---
title: PyUNO
summary: A complete single-player card game with AI opponents, tested game logic, responsive Pygame UI, and packaged desktop builds.
description: A complete single-player card game with AI opponents, tested game logic, responsive Pygame UI, and packaged desktop builds.
featured: false
order: 9
year: 2025
date: 2026-07-24
category: Software
area: ai-software
organization: Fachhochschule Südwestfalen
role: Group 19 course project with Jonathan Garry Hartono
stack:
  - Python
  - Pygame
  - Object-oriented design
  - CI packaging
repository: https://github.com/diovandi/PyUNO
cover: /assets/images/photos/pyuno-gameplay.webp
cover_width: 1600
cover_height: 1001
cover_alt: "PyUNO game screen on a red table: three AI opponents' face-down hands, the discard and draw piles in the centre, and the player's hand along the bottom."
cover_caption: "A turn against three AI opponents."
image: /assets/images/share/pyuno-gameplay.jpg
---

PyUNO implements a full game against three AI opponents, including the standard deck, special cards, turn direction, draw and discard piles, color choice, and an interactive “UNO!” quick-time event with penalties.

The code models cards, decks, players, and the overall game controller as separate classes. Unit tests cover the rule engine before it is connected to the Pygame interface, while the UI scales relative to the window dimensions and dynamically highlights legal moves.

<div class="photo-pair screenshots">
  <figure>
    <img src="{{ '/assets/images/photos/pyuno-choose-colour.webp' | relative_url }}" alt="PyUNO colour picker after a wild card, with red, yellow, green and blue squares over a dimmed table." width="1000" height="625" loading="lazy" decoding="async">
  </figure>
  <figure>
    <img src="{{ '/assets/images/photos/pyuno-uno-call.webp' | relative_url }}" alt="PyUNO with the player down to one card and the UNO! button showing." width="1000" height="625" loading="lazy" decoding="async">
  </figure>
</div>
<p class="photo-pair-caption">The colour picker after a wild card, and the timed “UNO!” call when a player is down to one card.</p>

## From source to desktop app

The repository includes PyInstaller build tooling, a working Windows executable, and automated Linux and macOS builds through GitHub Actions. Cross-platform asset paths, fonts, icons, and fallbacks are handled as part of the packaging workflow.

It began as a Basics in Python course project at FH-SWF and became a compact exercise in state machines, interface feedback, testing, and delivery.
