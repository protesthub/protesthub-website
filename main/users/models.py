from django.db import models

from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    """
    Default user profile
    """
    email = models.EmailField('email', max_length=255, unique=True)
    terms_of_use = models.BooleanField(default=False)
    newsletter = models.BooleanField(default=False)
