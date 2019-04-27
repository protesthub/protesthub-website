from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import check_password
from django.core.validators import validate_email, ValidationError


class User(AbstractUser):
    """
    Default user
    """
    email = models.EmailField('email', max_length=255, unique=True)
    terms_of_use = models.BooleanField(default=False)
    newsletter = models.BooleanField(default=False)


class UserBackend:
    @staticmethod
    def authenticate(request, username=None, password=None):
        """
        Authenticates a user by email org username and password.
        :param request:
        :param username: An email or username. If this is not called username authentication does not work?
        :param password:
        :return: Profile is email and password is valid otherwise None.
        """
        try:
            try:
                validate_email(username)
            except ValidationError:
                user = User.objects.get(username=username)
            else:
                user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        else:
            if check_password(password, user.password) is True:
                return user

        return None

    @staticmethod
    def get_user(user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
