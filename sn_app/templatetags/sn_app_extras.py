from django import template
import cloudinaryResponsive

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

# custom tag to render <picture> element from Cloudinary pictureID
@register.simple_tag
def pictureCloudinary(publicID, sizes, srcset, alt):
    # construct tuple from srcset string
    srcset = (i for i in srcset.split())
    return cloudinaryResponsive.pictureElement(publicID, sizes, srcset, alt)