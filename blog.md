---
title: Blog
permalink: /blog/
eyebrow: 02 / Notes
description: Writing about engineering, software, experiments, and what I learn while building.
---

<div class="post-list blog-index">
{% for post in site.posts %}
  <article class="post-row">
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%d %b %Y" }}</time>
    <div>
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p>{{ post.description | default: post.excerpt | strip_html | truncate: 180 }}</p>
      {% if post.tags %}
        <ul class="tag-list" aria-label="Topics">
          {% for tag in post.tags %}<li>{{ tag }}</li>{% endfor %}
        </ul>
      {% endif %}
    </div>
    <a class="row-arrow" href="{{ post.url | relative_url }}" aria-label="Read {{ post.title }}">→</a>
  </article>
{% endfor %}
</div>
