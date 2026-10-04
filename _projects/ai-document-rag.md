---
title: AI-Assisted Document Management & RAG
summary: A human-in-the-loop document workflow combining structured extraction, operational dashboards, status queries, and cited Drive-based answers.
featured: true
order: 1
year: 2026
category: AI systems
organization: PT Stratcon Agara Global
role: Corporate Development Intern
stack:
  - Python / Flask
  - Google Cloud Run
  - Gemini / Vertex AI
  - AppSheet
live_url: /projects/human-reviewed-ai-document-workflows/
live_label: Read the case study
---

During my corporate-development internship, I built a connected set of tools for finding, governing, and understanding operational documents.

The workflow used Google Apps Script and Gemini 2.0 Flash to extract structured metadata from Indonesian government permits, then routed uncertain results through human verification. AppSheet provided operational views, while Google Groups and Shared Drives formalized access and ownership for each department.

I also prototyped cited question-and-answer search over Google Drive using Vertex AI Search, and designed a Python/Flask WhatsApp assistant on Google Cloud Run for natural-language document-status queries, presented to leadership on 2 March 2026. These were built and piloted, not rolled out at scale. A separate meeting workflow used OpenAI Whisper and Gemini to produce transcripts, summaries, and speaker-assigned action items.

## Design priorities

- Keep source documents and citations visible instead of hiding uncertainty behind a generated answer.
- Separate machine extraction from human approval for consequential permit metadata.
- Make ownership and access governance part of the system architecture.
- Deliver the tools in channels people already use, including AppSheet and WhatsApp.

The full story, including what was built versus deployed, is in the [case study]({{ '/projects/human-reviewed-ai-document-workflows/' | relative_url }}). The implementation is internal, so this page documents the system boundaries and my contribution without exposing company data or private source code.
