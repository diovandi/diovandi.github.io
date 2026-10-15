---
title: Projects
permalink: /projects/
eyebrow: Portfolio
description: Engineering systems, research implementations, aerospace work, practical software, live production, and lab support—each grounded in project records, reports, public code, or recordings.
---

<p class="index-note">Projects marked as team work describe my documented role and contribution. Client and internal work is summarized without publishing confidential material.</p>

<div class="project-filter" role="group" aria-label="Filter projects by area" hidden>
  <button type="button" data-filter="all" aria-pressed="true">All</button>
{% for area in site.data.project_areas %}  <button type="button" data-filter="{{ area.key }}" aria-pressed="false">{{ area.label }}</button>
{% endfor %}</div>
<p class="project-filter-status" aria-live="polite"></p>

<div class="project-grid project-index">
{% assign sorted_projects = site.projects | sort: "order" %}
{% for project in sorted_projects %}
  {% include project-card.html project=project index=forloop.index heading="h2" %}
{% endfor %}
</div>
