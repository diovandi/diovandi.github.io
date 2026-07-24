---
title: Projects
permalink: /projects/
eyebrow: 01 / Portfolio
description: Engineering systems, research implementations, aerospace work, and practical software—each grounded in project records, reports, or public code.
---

<p class="index-note">Projects marked as team work describe my documented role and contribution. Client and internal work is summarized without publishing confidential material.</p>

<div class="project-grid project-index">
{% assign sorted_projects = site.projects | sort: "order" %}
{% for project in sorted_projects %}
  {% include project-card.html project=project index=forloop.index %}
{% endfor %}
</div>
