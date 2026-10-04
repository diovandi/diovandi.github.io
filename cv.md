---
title: CV
permalink: /cv/
eyebrow: CV
description: Education, experience, and selected work in one document.
---

{% if site.data.profile.cv_pdf %}
<p><a class="button button-primary" href="{{ site.data.profile.cv_pdf | relative_url }}">Download CV (PDF) <span aria-hidden="true">↓</span></a></p>
{% else %}
A downloadable CV is available on request. Please reach out on [LinkedIn]({{ site.data.profile.linkedin_url }}){% if site.data.profile.email %} or by email at [{{ site.data.profile.email }}](mailto:{{ site.data.profile.email }}){% endif %}.
{% endif %}

## In short

- **Now:** Strategic Technical Advisor at SAG, since August 2026.
- **Education:** S.T. in Mechanical Engineering (Mechatronics), Swiss German University, with a double-degree semester at FH Südwestfalen; earlier aerospace engineering coursework at TU Delft.
- **Focus:** AI-assisted engineering-document and data workflows with human review, grounded in PLC and control systems, mechanical design, and robotics.

The full timeline is on the [Experience]({{ '/experience/' | relative_url }}) page.
