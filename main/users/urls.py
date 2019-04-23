from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

from . import views
from .forms import SignInForm

app_name = 'users'
urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', LoginView.as_view(template_name='users/sign_in.html',
                                      redirect_field_name='/',
                                      authentication_form=SignInForm), name='sign_in'),
    path('sign_out', LogoutView.as_view(redirect_field_name='users:sign_in'), name='sign_out')
]
