---
layout: base
# title: Posts by Tag
---

{{page.url | absolute_url}}

{% assign tag_name = page.url | split: '/' | last %}
{% assign tag_posts = site.tags[tag_name] %}

{% if tag_posts %}
  <ul>
    {% for post in tag_posts %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% else %}
  <p>No posts found with the tag '{{ tag_name }}'.</p>
{% endif %}
