# Register your models here.
from django.contrib import admin

from .models import Demo
from main.users.models import Profile

admin.site.register(Demo)
admin.site.register(Profile)
