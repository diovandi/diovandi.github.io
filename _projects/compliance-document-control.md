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

I led the design and build, and the system is now in internal use.

### Work from the checklists people already use

I built it around SAG’s actual checklists for environmental work, company and transport requirements, and iron-and-steel imports. They weren’t laid out the same way or written with the same terminology, and the app had to handle those differences without making staff start from scratch for every project. A company can have several projects, and each project several checklists, which staff can reuse or revise for later work.

The original wording and workbook references stay attached to each imported requirement so people can check where it came from. A tick in a spreadsheet still needs interpreting: it tells us what someone recorded, not that the app has received and approved that file. Rows appearing one after another also don’t necessarily mean one depends on the other. Those dependencies need review.

### Show what’s blocking the next step

Some requirements depend on other documents or information, so a completion percentage alone doesn’t tell staff enough: one missing input could be the thing stopping the next step. The system separates the requirement, its inputs and the stage they allow to proceed. Staff can keep preparing other parts of a project while a submission step is blocked, and see what is blocking it.

Approving a document is also different from accepting it for a particular project. A company document may be reusable, but someone still needs to check that the exact approved version meets this project’s requirement, and the app records that decision separately.

### Review responsibilities and new revisions

<figure class="diagram">
  {% include diagrams/document-control-review.svg %}
  <figcaption>The review chain, and what happens when a newer file is uploaded. A simplified diagram, not a screenshot of the system.</figcaption>
</figure>

Uploading a newer file shouldn’t silently replace the version a project already relies on. Submitted content stays fixed and a material change becomes a new revision. Adopting it is another review decision. Checklist changes work the same way: updating a template doesn’t quietly change the requirements of an active project. AI extraction can help prepare information for review, but it doesn’t approve a file or decide that a project is ready.

### Keeping it usable

My main priorities were seeing missing items and tracking staff work. I asked for English and Bahasa Indonesia because people at SAG have different levels of comfort with English; the instructions are simple in both, while keeping the original permit names and source wording. I left fees out of the first release.

Colleagues and AI development tools contributed to this work. The documented checks include local and browser testing and reviewed code changes. I don’t have before-and-after measurements for processing time, adoption or errors.

## Procurement and budget app

The office runs its purchasing on an internal app built mostly by a colleague. I contributed through reviewed pull requests: monthly budget pots, clearer admin controls, the brand and a compact bilingual interface, CI fixes, a deploy guard, and a shared rules file for the people and AI coding agents who work on the codebase.

## Skills and knowledge tools

- Claude skills that produce on-brand company documents and meeting minutes, later merged into the company repository.
- A knowledge graph of company material, with integrity checks, used as a navigation aid.
- A checklist-compliance checker for import/export and AMDAL environmental requirements, which I led and which is now in internal use.

The code is internal, so this page describes the system and my part in it without company data or source. For how human review shapes these systems, see the [case study]({{ '/projects/human-reviewed-ai-document-workflows/' | relative_url }}).
