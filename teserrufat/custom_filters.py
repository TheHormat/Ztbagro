from django import template

register = template.Library()

@register.filter(name="remove_spaces")
def remove_spaces(value):
    return value.replace(" ", "")