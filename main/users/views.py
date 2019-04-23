from django.contrib.auth.models import User
from django.shortcuts import render

from .forms import SignUpForm


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'])
            user.profile.terms_of_use = form.cleaned_data['terms_of_use']
            user.profile.newsletter = form.cleaned_data['newsletter']
            user.save()
    else:
        form = SignUpForm()

    return render(request, 'users/sign_up.html', {'form': form})
