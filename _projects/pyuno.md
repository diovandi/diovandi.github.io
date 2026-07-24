---
title: PyUNO
summary: A complete single-player card game with AI opponents, tested game logic, responsive Pygame UI, and packaged desktop builds.
featured: false
order: 9
year: 2025
category: Software
organization: Fachhochschule Südwestfalen
role: Group 19 course project with Jonathan Garry Hartono
stack:
  - Python
  - Pygame
  - Object-oriented design
  - CI packaging
repository: https://github.com/diovandi/PyUNO
---

PyUNO implements a full game against three AI opponents, including the standard deck, special cards, turn direction, draw and discard piles, color choice, and an interactive “UNO!” quick-time event with penalties.

The code models cards, decks, players, and the overall game controller as separate classes. Unit tests cover the rule engine before it is connected to the Pygame interface, while the UI scales relative to the window dimensions and dynamically highlights legal moves.

## From source to desktop app

The repository includes PyInstaller build tooling, a working Windows executable, and automated Linux and macOS builds through GitHub Actions. Cross-platform asset paths, fonts, icons, and fallbacks are handled as part of the packaging workflow.

It began as a Basics in Python course project at FH-SWF and became a compact exercise in state machines, interface feedback, testing, and delivery.
