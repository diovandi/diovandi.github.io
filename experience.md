---
title: Experience
permalink: /experience/
eyebrow: 03 / Experience
description: A timeline spanning teaching, industrial training, mechanical design, AI-enabled workflows, aerospace programs, and technical leadership.
---

<div class="timeline">
{% for role in site.data.experience %}
  <article class="timeline-item">
    <div class="timeline-side">
      <span>{{ role.period }}</span>
      <span>{{ role.location }}</span>
    </div>
    <div class="timeline-content">
      <p class="timeline-organization">{{ role.organization }}</p>
      <h2>{{ role.role }}</h2>
      <p>{{ role.summary }}</p>
      {% if role.highlights %}
        <ul>
          {% for highlight in role.highlights %}<li>{{ highlight }}</li>{% endfor %}
        </ul>
      {% endif %}
    </div>
  </article>
{% endfor %}
</div>

<h2>Education</h2>

<div class="education-grid">
  <article>
    <span>2023–2026</span>
    <h3>Swiss German University</h3>
    <p>Mechanical Engineering, Mechatronics concentration. Final thesis on a CAD-integrated mechanical assembly rating tool based on Kinematic Screw Theory.</p>
  </article>
  <article>
    <span>2025</span>
    <h3>Fachhochschule Südwestfalen</h3>
    <p>International Industrial Engineering semester in Soest through the SGU double-degree pathway.</p>
  </article>
  <article>
    <span>2019–2023</span>
    <h3>Delft University of Technology</h3>
    <p>Coursework toward a BSc in Aerospace Engineering, including aircraft design, structures, and test analysis; credits later transferred to SGU.</p>
  </article>
</div>

<h2>Selected recognition & service</h2>

<div class="recognition-grid">
  <article><strong>2nd place</strong><span>EBEC Challenge Delft 2023, Case Study category</span></article>
  <article><strong>€15,625+</strong><span>Stratos IV crowdfunding campaign</span></article>
  <article><strong>US$4,000</strong><span>Raised for Education Above All as a high-school fundraising coordinator</span></article>
  <article><strong>2024–2025</strong><span>Head of Academics, SGU Mechatronics student association</span></article>
</div>
