from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from .models import Profile


class SignUpForm(forms.Form):
    username = forms.CharField(label='Your username', max_length=100, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='Your email', required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='Your password', max_length=100, required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    terms_of_use = forms.BooleanField(required=True)
    newsletter = forms.BooleanField(required=False)

    def clean_email(self):
        data = self.cleaned_data['email']

        if Profile.objects.filter(email=data).count() > 0:
            raise forms.ValidationError('Email already taken.')

        return data


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate', 'placeholder': 'Email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))
