---
title: "Case study: Human-reviewed AI document workflows"
summary: How I built AI tools that read operational documents while keeping a person responsible for every record that matters. A two-minute read.
order: 1.5
year: 2026
category: Case study
organization: PT Stratcon Agara Global (SAG)
role: Corporate Development Intern (2026) · Strategic Technical Advisor
stack:
  - Apps Script / Gemini
  - Python / Flask
  - Google Cloud Run
  - AppSheet
---

<!--
  TODO(Dio) before merging:
  - Confirm with SAG that a redacted version may be published.
  - Deployment statuses follow the CV wording (built / prototyped / in trials); check against SAG records.
  - Confirm the contribution statement, and name anything that was a teammate's.
  - Add 2–3 redacted screenshots (no client names, permit numbers, or people).
-->

## The problem

Operational documents, including government permits, lived in shared folders. Turning them into searchable records by hand is slow, and letting an AI fill those records alone is too risky when they carry legal consequences. The goal was faster retrieval without giving up human accountability.

## The approach

AI does the reading; people make the decisions. The system extracts metadata, flags anything it is unsure of, and a reviewer approves it before it becomes a record anyone relies on. Questions are answered from those approved records or from the source files, with a citation back to the document.

<figure class="diagram">
  <img src="{{ '/assets/images/case-studies/human-reviewed-ai-architecture.svg' | relative_url }}" alt="Architecture: source documents feed an AI extraction step; a human reviews uncertain fields before records are approved; staff query approved records through a dashboard and a chat assistant that cites its sources.">
  <figcaption>System architecture, simplified. No company data is shown.</figcaption>
</figure>

<!-- TODO(Dio): add 2–3 redacted screenshots here, e.g.
<figure>
  <img src="{{ '/assets/images/case-studies/review-queue-redacted.webp' | relative_url }}" alt="…">
  <figcaption>…</figcaption>
</figure>
-->

## Built versus deployed

| Component | Status |
| --- | --- |
| Permit metadata extraction (Apps Script + Gemini) with human verification and AppSheet review views | Built; not rolled out at scale |
| Cited document Q&A over Google Drive (Vertex AI Search) | Prototyped |
| Document-status assistant (Python/Flask on Cloud Run, via WhatsApp) | Designed and presented; live use not verified |
| Versioned document-control and readiness tracking (Cloudflare Workers + D1) | Implemented and locally tested |
| Checklist-compliance checker for import/export and environmental (AMDAL) requirements | In trials |

There is no measured time-saving baseline yet, so this page makes no efficiency claims. The work was presented to company leadership on 2 March 2026.

## My contribution

<!-- TODO(Dio): confirm this sentence. -->
I built the permit-extraction workflow with its human-review step and AppSheet views, prototyped the cited Q&A, and designed the document-status assistant during my internship (January to March 2026). As Strategic Technical Advisor since August 2026, I specified and implemented the document-control system and am developing the compliance checker.

## Lessons

<!-- TODO(Dio): these are drafted from the design priorities; replace with what you actually learned. -->
- **Review is a design feature, not a fallback.** Deciding which fields need a person shapes the whole data model.
- **Show the source.** An answer that links back to its document is easier to check than one that only sounds confident.
- **Meet people where they already work.** The tools ran in a dashboard and a chat channel rather than a new application.
- **Access control is part of the architecture.** Ownership of the shared drives had to be settled before any AI could read them.

Company documents, client names, and identifiers are deliberately left out. For the broader set of tools, see [AI-Assisted Document Management & RAG]({{ '/projects/ai-document-rag/' | relative_url }}).
