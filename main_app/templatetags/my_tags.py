from django import template
from django_bootstrap5.templatetags.django_bootstrap5 import bootstrap_form

register = template.Library()

@register.simple_tag(takes_context=True)
def bootstrap_formset(context, formset, **kwargs):
    return bootstrap_form(context['request'], formset, **kwargs)