from django import forms
from models import ContactMe, Photo
from widgets import PhotoAdminThumbWidget

class PhotoAdminForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = '__all__'
        widgets = {
            'thumbnail_url': PhotoAdminThumbWidget(),
        }

class ContactMeForm(forms.ModelForm):
    name = forms.CharField(
                                label='Your name',
                                widget=forms.TextInput(
                                                    attrs={
                                                    'id': 'post-name',
                                                    'placeholder': 'your name',
                                                    'name': 'name',
                                                    'required': 'required',
                                                    'autocomplete': 'on',
                                                    'maxlength': '100',
                                                    'aria-label': 'Your name'
                                                    }
                                                    )
                                )
    email = forms.CharField(
                                label='Your e-mail',
                                widget=forms.EmailInput(
                                                    attrs={
                                                    'id': 'post-email',
                                                    'placeholder':'email@example.com',
                                                    'name': 'email',
                                                    'required': 'required',
                                                    'autocomplete': 'on',
                                                    'maxlength': '254',
                                                    'aria-label': 'Your email'
                                                    }
                                                    )
                                )
    message = forms.CharField(
                            label='Your message',
                            widget=forms.Textarea(
                                                attrs={
                                                'id': 'post-message',
                                                'placeholder':'your message...',
                                                'maxlength': '2000',
                                                'aria-label': 'Your message',
                                                'required': 'required'
                                                #'pattern': '^.{1,2000}$'
                                                }
                                                )
                            )
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = ContactMe
        exclude = ['time_sent']
