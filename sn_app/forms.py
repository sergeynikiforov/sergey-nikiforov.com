from django import forms
from models import ContactMe

class ContactMeForm(forms.ModelForm):
    name = forms.CharField(
                                label='Your name',
                                widget=forms.TextInput(
                                                    attrs={
                                                    'placeholder': 'your name',
                                                    'name': 'name',
                                                    'required autocomplete': 'name',
                                                    'maxlength': '100',
                                                    'aria-label': 'Your name'
                                                    }
                                                    )
                                )
    email = forms.CharField(
                                label='Your e-mail',
                                widget=forms.EmailInput(
                                                    attrs={
                                                    'placeholder':'email@example.com',
                                                    'name': 'email',
                                                    'required autocomplete': 'email',
                                                    'maxlength': '254',
                                                    'aria-label': 'Your email'
                                                    }
                                                    )
                                )
    message = forms.CharField(
                            label='Your message',
                            widget=forms.Textarea(
                                                attrs={
                                                'placeholder':'your message...',
                                                'maxlength': '2000',
                                                'aria-label': 'Your message'
                                                }
                                                )
                            )
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = ContactMe
        exclude = ['time_sent']
