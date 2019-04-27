from django.shortcuts import HttpResponseRedirect, render

from .forms import SignUpForm
from .models import User


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'],
                                            terms_of_use=form.cleaned_data['terms_of_use'],
                                            newsletter=form.cleaned_data['newsletter'])
            user.save()

            return HttpResponseRedirect("/")
    else:
        form = SignUpForm()

    return render(request, 'users/sign_up.html', {'form': form})
