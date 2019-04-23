from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import check_password
from django.core.validators import validate_email, ValidationError


class Profile(AbstractUser):
    """
    Default user profile
    """
    email = models.EmailField('email', max_length=255, unique=True)
    terms_of_use = models.BooleanField(default=False)
    newsletter = models.BooleanField(default=False)


class ProfileBackend:
    def authenticate(self, request, username=None, password=None):
        """
        Authenticates a user by email org username and password.
        TODO: Sanitize input data and check if it is an email. This should already be checked by a form, but better we
        TODO: have more layers of security.
        :param request:
        :param username: An email or username. TODO If this is not called username authentication does not work?
        :param password:
        :return: Profile is email and password is valid otherwise None.
        """
        try:
            try:
                validate_email(username)
            except ValidationError:
                user = Profile.objects.get(username=username)
            else:
                user = Profile.objects.get(email=username)
        except Profile.DoesNotExist:
            return None
        else:
            if check_password(password, user.password) is True:
                return user

        return None

    def get_user(self, user_id):
        try:
            return Profile.objects.get(pk=user_id)
        except Profile.DoesNotExist:
            return None
