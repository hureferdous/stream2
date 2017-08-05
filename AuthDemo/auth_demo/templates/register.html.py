{% extends "base.html" %}
{% load bootstrap_tags %}
{% block content %}
    <form role="form" method="post" action="{% url 'register' %}">
        <legend>Create a new account</legend>
        {% csrf_token %}
        {{ form | as_bootstrap }}
        <div class="form-group">
            <button type="submit" class="btn btn-primary">Create account</button>
        </div>
    </form>
{% endblock %}