---
layout: default
title: MC Software ltd — Small studio. Native apps.
description: Independent iOS studio founded by Matteo Comisso. Makers of EchoAI, Weekwise, and My Vinyl.
---

<section class="home-hero">
  <div class="container">
    <h1 class="home-hero__title">Small studio. Native apps.</h1>
    <p class="home-hero__sub">MC Software ltd is an independent studio building thoughtful, on-device apps for iOS and the Mac.</p>
  </div>
</section>

<section class="projects-section">
  <div class="container">
    <div class="projects-section__heading">
      <p class="projects-section__label">Projects</p>
      <p class="projects-section__count">{{ site.data.projects | size | prepend: "00" | slice: -3, 3 }} &nbsp;/&nbsp; Shipped &amp; in progress</p>
    </div>
    <ul class="project-list">
    {%- for project in site.data.projects -%}
      <li>{% include project_card.html project=project %}</li>
    {%- endfor -%}
    </ul>
  </div>
</section>
