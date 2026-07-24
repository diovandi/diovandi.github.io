---
title: Research & technical writing
permalink: /publications/
eyebrow: 02 / Writing
description: Papers, thesis work, and selected technical reports. Course papers and manuscripts are labeled as such rather than presented as peer-reviewed publications.
---

<div class="publication-list publication-index">
{% assign sorted_publications = site.publications | sort: "order" %}
{% for publication in sorted_publications %}
  {% include publication-card.html publication=publication %}
{% endfor %}
</div>
