---
title: Projects
permalink: /projects/
eyebrow: 01 / Portfolio
description: Selected engineering and software projects, from mechanical assembly analysis to small experiments built for the joy of making.
---

<div class="project-grid project-index">
{% assign sorted_projects = site.projects | sort: "order" %}
{% for project in sorted_projects %}
  {% include project-card.html project=project index=forloop.index %}
{% endfor %}
</div>
