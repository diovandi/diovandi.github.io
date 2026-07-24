---
title: AI-Assisted Document Management & RAG
summary: A human-in-the-loop document workflow combining structured extraction, operational dashboards, status queries, and cited Drive-based answers.
featured: true
order: 3
year: 2026
category: AI systems
organization: PT Stratcon Agara Global
role: Corporate Development Intern
stack:
  - Python / Flask
  - Google Cloud Run
  - Gemini / Vertex AI
  - AppSheet
---

During my corporate-development internship, I built a connected set of tools for finding, governing, and understanding operational documents.

The workflow used Google Apps Script and Gemini 2.0 Flash to extract structured metadata from Indonesian government permits, then routed uncertain results through human verification. AppSheet provided operational views, while Google Groups and Shared Drives formalized access and ownership across Core, Legal, Finance, and Administration.

I also developed a Python/Flask WhatsApp bot on Google Cloud Run. It answered natural-language document-status questions and supported retrieval-augmented Q&A with citations back to the relevant Google Drive sources. A separate meeting workflow used OpenAI Whisper and Gemini to produce transcripts, summaries, and speaker-assigned action items.

## Design priorities

- Keep source documents and citations visible instead of hiding uncertainty behind a generated answer.
- Separate machine extraction from human approval for consequential permit metadata.
- Make ownership and access governance part of the system architecture.
- Deliver the tools in channels people already use, including AppSheet and WhatsApp.

The implementation is internal, so this page documents the system boundaries and my contribution without exposing company data or private source code.
