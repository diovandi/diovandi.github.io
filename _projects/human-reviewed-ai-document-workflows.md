---
title: "Case study: Human-reviewed AI document workflows"
summary: How I built AI tools that read operational documents while keeping a person responsible for every record that matters. A two-minute read.
order: 1.5
year: 2026
category: Case study
organization: PT Stratcon Agara Global (SAG)
role: Corporate Development Intern, now Strategic Technical Advisor
stack:
  - Apps Script / Gemini
  - Python / Flask
  - Google Cloud Run
  - AppSheet
---

<!--
  TODO(Dio) before merging:
  - Confirm with SAG that a redacted version may be published.
  - Replace the deployment-status cells below with what SAG's records say.
  - Confirm the one-line contribution statement.
  - Add 2–3 redacted screenshots (no client names, permit numbers, or people).
-->

## The problem

Operational documents, including government permits, lived in shared folders. Turning them into searchable records by hand is slow, and letting an AI fill those records alone is too risky when they carry legal consequences. The goal was faster retrieval without giving up human accountability.

## The approach

AI does the reading; people make the decisions. The system extracts metadata, flags anything it is unsure of, and a reviewer approves it before it becomes a record anyone relies on. Questions are answered from those approved records or from the source files, always with a citation back to the document.

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

| Component | Built | Deployment status |
| --- | --- | --- |
| Permit metadata extraction with human review | Yes | To be confirmed from SAG records |
| AppSheet status dashboard | Yes | To be confirmed from SAG records |
| Chat assistant for document status and cited answers | Yes | To be confirmed from SAG records |
| Meeting transcription and action-item summaries | Yes | To be confirmed from SAG records |
| Group-based access and ownership for shared drives | Yes | To be confirmed from SAG records |

The work was presented to company leadership on 2 March 2026.

## My contribution

<!-- TODO(Dio): confirm this sentence. -->
I designed and built the extraction workflow, the human-review step, the dashboard, and the chat assistant during my internship.

## Lessons

<!-- TODO(Dio): these are drafted from the design priorities; replace with what you actually learned. -->
- **Review is a design feature, not a fallback.** Deciding which fields need a person shapes the whole data model.
- **Show the source.** An answer that links back to its document is easier to check than one that only sounds confident.
- **Meet people where they already work.** The tools ran in a dashboard and a chat channel rather than a new application.
- **Access control is part of the architecture.** Ownership of the shared drives had to be settled before any AI could read them.

Company documents, client names, and identifiers are deliberately left out. For the broader set of tools, see [AI-Assisted Document Management & RAG]({{ '/projects/ai-document-rag/' | relative_url }}).
