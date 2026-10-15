---
title: Compliance Document Control & Internal Tools
summary: A document-control system for compliance projects on Cloudflare Workers and D1, plus contributions to a live procurement app and Claude skills for company documents.
description: A document-control system for compliance projects on Cloudflare Workers and D1, plus contributions to a live procurement app and Claude skills for company documents.
featured: false
related:
  - /projects/human-reviewed-ai-document-workflows/
order: 1.6
year: 2026
date: 2026-10-14
category: AI systems
area: ai-software
organization: PT Stratcon Agara Global (SAG)
role: Strategic Technical Advisor
stack:
  - Cloudflare Workers
  - Cloudflare D1
  - Google Drive API
  - Claude skills
---

As Strategic Technical Advisor at Stratcon Agara Global, I built internal software for an advisory firm whose compliance projects run on permits, regulatory checklists, and many revisions of the same documents.

## Document control

The main system I built tracks every document a compliance project needs and what state it is in. It runs on Cloudflare Workers with a D1 database and handles:

- three-tier approvals and revision history, with an audit trail of who changed what;
- readiness tracking against reusable checklists, so a project lead can see what is still missing;
- import of the team's existing Excel regulatory checklists instead of retyping them;
- file storage in Google Drive, where the team already keeps its documents.

The system is built and browser-tested locally; it has not been deployed to the whole office.

## Procurement and budget app

The office runs its purchasing on an internal app built mostly by a colleague. I contributed through reviewed pull requests: monthly budget pots, clearer admin controls, the brand and a compact bilingual interface, CI fixes, a deploy guard, and a shared rules file for the people and AI coding agents who work on the codebase.

## Skills and knowledge tools

- Claude skills that produce on-brand company documents and meeting minutes, later merged into the company repository.
- A knowledge graph of company material, with integrity checks, used as a navigation aid.
- A checklist-compliance checker for import/export and AMDAL environmental requirements, taken to trial stage.

The code is internal, so this page describes the system and my part in it without company data or source. For how human review shapes these systems, see the [case study]({{ '/projects/human-reviewed-ai-document-workflows/' | relative_url }}).
