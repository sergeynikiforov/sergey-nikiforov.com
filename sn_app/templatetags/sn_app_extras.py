from django import template

register = template.Library()

# custom filter to access dict values by keys when a key is a variable
@register.filter(name='key')
def key(d, key_name):
    try:
        value = d[key_name]
    except KeyError:
        from django.conf import settings
        value = settings.TEMPLATE_STRING_IF_INVALID

    return value
