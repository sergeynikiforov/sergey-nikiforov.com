from django import forms
from models import ContactMe

class ContactMeForm(forms.ModelForm):
    name = forms.CharField(
                                label='Your name',
                                widget=forms.TextInput(
                                                    attrs={
                                                    'placeholder': 'John Smith',
                                                    'name': 'name',
                                                    'required autocomplete': 'name',
                                                    'maxlength': '100'
                                                    }
                                                    )
                                )
    email = forms.CharField(
                                label='Your e-mail',
                                widget=forms.EmailInput(
                                                    attrs={
                                                    'placeholder':'johnsmith@example.com',
                                                    'name': 'email',
                                                    'required autocomplete': 'email',
                                                    'maxlength': '254'
                                                    }
                                                    )
                                )
    message = forms.CharField(
                            label='Your message',
                            widget=forms.Textarea(
                                                attrs={
                                                'placeholder':'Your message goes here...',
                                                'maxlength': '2000'
                                                }
                                                )
                            )
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = ContactMe
        exclude = ['time_sent']
