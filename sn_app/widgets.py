from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class PhotoAdminThumbWidget(forms.widgets.URLInput):

    template_name = 'sn_app/photo_admin_thumb_widget.html'

    def render(self, name, value, attrs=None):
        context = {
            'url': value,
            'title': name
        }
        html = super(PhotoAdminThumbWidget, self).render(name, value, attrs)
        html += render_to_string(self.template_name, context)
        return mark_safe(html)
