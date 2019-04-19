from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(label='Your username', max_length=100, required=True)
    email = forms.EmailField(label='Your email', required=True)
    password = forms.CharField(label='Your password', max_length=100, required=True)

