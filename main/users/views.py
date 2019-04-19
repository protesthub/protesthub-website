from django.contrib.auth.models import User
from django.shortcuts import render

from .forms import SignUpForm


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'],
                                            form.cleaned_data['email'],
                                            form.cleaned_data['password'])
        else:
            form = SignUpForm

    return render(request, 'users/sign_up.html')
