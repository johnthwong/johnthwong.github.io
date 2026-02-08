---
layout: default
---

<nav class="tabs">
   <button class="tab-btn active" data-tab="microsimulation">Microsimulation</button>
   <button class="tab-btn" data-tab="blogs">Research Notes</button>
   <button class="tab-btn" data-tab="working-papers">Working Papers</button>
</nav>

<button id="sort-toggle" class="sort-btn" style="display:none">Sort: Custom</button>

<div class="tab-content">

<div id="microsimulation" class="tab-panel active">
{% for item in site.data.microsimulation %}
<div class="card" data-date="{{ item.date }}" data-order="{{ forloop.index }}">
   <h3>{{ item.title }}</h3>
   {% if item.date %}<span class="card-date">{% if item.date_label %}{{ item.date_label | upcase }} {% endif %}DATE: {{ item.date }}</span>{% endif %}
   <p>{{ item.description }}</p>
   {% if item.html %}<a class="btn-more" href="{{ item.html }}">More</a>{% endif %}
   {% if item.image %}<div class="card-img-wrapper"><img src="{{ item.image | relative_url }}" alt="{{ item.title }}"></div>{% endif %}
   {% if item.features %}<p class="card-cites" data-features='[{% for f in item.features %}{"pub":"{{ f.publication }}","link":"{{ f.link }}"}{% unless forloop.last %},{% endunless %}{% endfor %}]'></p>{% endif %}
</div>
{% endfor %}
</div>

<div id="blogs" class="tab-panel">
{% for item in site.data.blogs %}
<div class="card" data-date="{{ item.date }}" data-order="{{ forloop.index }}">
   <h3>{{ item.title }}</h3>
   {% if item.date %}<span class="card-date">{% if item.date_label %}{{ item.date_label | upcase }} {% endif %}DATE: {{ item.date }}</span>{% endif %}
   <p>{{ item.description }}</p>
   {% if item.html %}<a class="btn-more" href="{{ item.html }}">More</a>{% endif %}
   {% if item.image %}<div class="card-img-wrapper"><img src="{{ item.image | relative_url }}" alt="{{ item.title }}"></div>{% endif %}
   {% if item.features %}<p class="card-cites" data-features='[{% for f in item.features %}{"pub":"{{ f.publication }}","link":"{{ f.link }}"}{% unless forloop.last %},{% endunless %}{% endfor %}]'></p>{% endif %}
</div>
{% endfor %}
</div>

<div id="working-papers" class="tab-panel">
{% for item in site.data.working_papers %}
<div class="card" data-date="{{ item.date }}" data-order="{{ forloop.index }}">
   <h3>{{ item.title }}</h3>
   {% if item.date %}<span class="card-date">{% if item.date_label %}{{ item.date_label | upcase }} {% endif %}DATE: {{ item.date }}</span>{% endif %}
   <p>{{ item.description }}</p>
   {% if item.html %}<a class="btn-more" href="{{ item.html }}">More</a>{% endif %}
   {% if item.image %}<div class="card-img-wrapper"><img src="{{ item.image | relative_url }}" alt="{{ item.title }}"></div>{% endif %}
   {% if item.features %}<p class="card-cites" data-features='[{% for f in item.features %}{"pub":"{{ f.publication }}","link":"{{ f.link }}"}{% unless forloop.last %},{% endunless %}{% endfor %}]'></p>{% endif %}
</div>
{% endfor %}
</div>

</div>
