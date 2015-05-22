from django.forms import ModelForm
from models import ContactMe

class ContactMeForm(ModelForm):
    class Meta:
        model = ContactMe
        exclude = ['time_sent']
