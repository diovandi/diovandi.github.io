---
title: "Opportunity Control Room: a job-search dashboard"
summary: A private dashboard for jobs, applications, CVs and cover letters, built with AI coding agents and then cut back to the compact view I actually use.
description: A private job-search dashboard on Cloudflare Workers, D1 and R2 that keeps fit, listing status and application stage separate, built with AI coding agents.
featured: false
order: 1.8
related:
  - /projects/compliance-document-control/
year: 2026
date: 2026-10-21
category: Personal software
area: ai-software
organization: Personal project
role: Product owner · Built with AI coding agents
stack:
  - React
  - Cloudflare Workers
  - Cloudflare D1 / R2
  - GitHub Actions
---

I built the Opportunity Control Room with AI coding agents to keep track of jobs, applications, CVs and cover letters. My search covers quite a few different areas, so I wanted somewhere to put the listings and compare them against what I’ve actually done.

By October, I was still tracking applications in Excel, and the dashboard had become too bloated to be useful. There was too much going on. I didn’t need a blurb under every button or an explanation of the Sankey diagram every time I opened it. I needed filters, a compact view and a clear idea of where my applications stood.

## Getting back to the actual task

I asked for the Applications table to become the default, with search and filters that worked together. The extra reference views and charts could stay available without all being open at once.

That meant removing a lot of text, folding away the less-used views and making progress easier to see. The immediate task is fairly simple: find a job, check what I know about it, and work out what I need to do next.

## A good fit doesn’t mean the listing is open

A job might fit my background but have an unclear listing status. I might have a CV and letter ready without having applied. Those need their own fields, otherwise the totals stop meaning much.

<figure class="diagram">
  {% include diagrams/ocr-fields.svg %}
  <figcaption>The four fields recorded for each job. The labels are the ones the dashboard shows.</figcaption>
</figure>

One example was a role marked unverified even though I could still see the employer’s listing. I questioned it, and the investigation found it had been missed in a verification update. The correction had to go into the live database and its history: changing the example data in the repository wouldn’t update a database that was already populated.

The dashboard now records fit, listing status, employer verification and application progress separately, with source links and verification dates. Preparing a letter doesn’t mark the job as Applied.

## Choosing the right experience for a job

I also wanted it to select a suitable CV and prepare a cover letter. It chooses an existing source CV and creates a separate editable letter from checked facts about my experience. It keeps the original CV and records which version the draft used.

The job description helps decide which experience to bring forward. It can’t supply experience I don’t have. An AV technician role should bring up my camera, streaming and production work; a lab role should bring up printer support and teaching. Matching both on the word “technician” would miss the point.

Saved letters have revision checks, so an older edit can’t silently overwrite a newer one. Generating another draft keeps the earlier draft and the CV it used.

## What went into the build

The dashboard is private and separate from this website. It uses React on Cloudflare Workers, with D1 for the records and R2 for private CV files. The app and document downloads check who is accessing them.

GitHub Actions runs the checks and deploys main with a commit ID. Database changes use migrations that preserve existing records. These are my application notes and documents, so they need to survive changes to the app.

AI agents did a substantial amount of the implementation. I set the requirements, challenged the interface, supplied and corrected the career facts, and reviewed the results.

## Where it stands

The current version has the compact interface, saved application packs, CV versions, revision checks and private exports. The letters use reviewed templates. External AI generation, automatic job discovery, email intake and scheduled processing are planned features, not things the dashboard runs today. I don’t have a measured improvement in application outcomes to attach to it.
