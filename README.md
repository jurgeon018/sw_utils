

## Set language 

templates/projects/header.html
{% get_current_language as LANGUAGE_CODE %}
{% get_available_languages as LANGUAGES %}
{% get_language_info_list for LANGUAGES as languages %}
{% for language in languages %}
<a href="{% url 'set_lang' language.code %}">
<div class="nav-lang {% if language.code == LANGUAGE_CODE %}active{% endif %}">
  {% if  language.code == 'uk' %}
    Ukr
  {% elif language.code == 'ru' %}
    Rus
  {% elif language.code == 'en' %}
    Eng
  {% endif %}
</div>
</a>
{% endfor %}


