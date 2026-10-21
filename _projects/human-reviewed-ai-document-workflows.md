---
title: "Case study: Human-reviewed AI document workflows"
description: How I built AI extraction, cited search and document-control tools for permits and compliance documents, with a person reviewing every record that matters.
summary: How I built AI tools that read operational documents while keeping a person responsible for every record that matters. A two-minute read.
featured: true
order: 1
related:
  - /projects/compliance-document-control/
redirect_from:
  - /projects/ai-document-rag/
year: 2026
date: 2026-10-14
category: Case study
area: ai-software
organization: PT Stratcon Agara Global (SAG)
role: Corporate Development Intern (2026) · Strategic Technical Advisor
stack:
  - Apps Script / Gemini
  - Python / Flask
  - Google Cloud Run
  - AppSheet
---

## The problem

Operational documents, including government permits, lived in shared folders. Turning them into searchable records by hand is slow, and letting an AI fill those records alone is too risky when they carry legal consequences. The goal was faster retrieval without giving up human accountability.

## The approach

AI does the reading; people make the decisions. The system extracts metadata, flags anything it is unsure of, and a reviewer approves it before it becomes a record anyone relies on. Questions are answered from those approved records or from the source files, with a citation back to the document. Google Groups and Shared Drives set who owns and can read each department's files.

<figure class="diagram">
  <img src="{{ '/assets/images/case-studies/human-reviewed-ai-architecture.svg' | relative_url }}" alt="Architecture: source documents feed an AI extraction step; a human reviews uncertain fields before records are approved; staff query approved records through a dashboard and a chat assistant that cites its sources.">
  <figcaption>System architecture, simplified. No company data is shown.</figcaption>
</figure>

## Built versus deployed

| Component | Status |
| --- | --- |
| Permit metadata extraction (Apps Script + Gemini 2.0 Flash) with human verification and AppSheet review views | Built; production deployment was pending when the internship ended in March 2026 |
| Cited document Q&A over Google Drive (Vertex AI Search) | Prototyped |
| Document-status assistant (Python/Flask on Cloud Run, via WhatsApp) | Designed and presented; live use not verified |
| Versioned document-control and readiness tracking (Cloudflare Workers + D1) | Built; now in internal use |
| Checklist-compliance checker for import/export and environmental (AMDAL) requirements | Built; now in internal use |
| Meeting-transcription pipeline (Whisper) | Built |

There is no measured time-saving baseline yet, so this page makes no efficiency claims. The work was presented to company leadership on 2 March 2026.

## My contribution

I built the permit-extraction workflow with its human-review step and AppSheet views, prototyped the cited Q&A, and designed the document-status assistant during my internship (January to March 2026). As Strategic Technical Advisor from August to October 2026, I led the document-control system and the checklist-compliance checker, both now in internal use.

## Design principles

- **Review is part of the design.** The system flags the fields it is unsure of, and a reviewer approves each record before anyone relies on it.
- **Show the source.** Answers come from approved records or source files, with a citation back to the document.
- **Access follows ownership.** Google Groups and Shared Drives set who owns and can read each department's files.

Company documents, client names, and identifiers are deliberately left out. The document-control system and other internal tools are described in [Compliance Document Control & Internal Tools]({{ '/projects/compliance-document-control/' | relative_url }}).
