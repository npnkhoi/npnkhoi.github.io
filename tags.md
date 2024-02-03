---
layout: base
---

<h1>Posts by tags</h1>
<ul class="tags">
{% for tag in site.tags %}
  {% assign t = tag | first %}
  {% assign posts = tag | last %}
  <a href="#{{ t | downcase | url_encode }}/" >{{ t | downcase }}</a> ({{ posts | size }})
{% endfor %}
</ul>

{% for tag in site.tags %}
  {% assign t = tag | first %}
  {% assign posts = tag | last %}

<h2>
  <a href="#{{ t | downcase | url_encode }}/" id="{{ t | downcase | url_encode }}/" >{{ t | downcase }}</a>
</h2>
<ul>
{% for post in posts %}
  {% if post.tags contains t %}
  <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <span class="date">{{ post.date | date: "%B %-d, %Y"  }}</span>
  </li>
  {% endif %}
{% endfor %}
</ul>
{% endfor %}