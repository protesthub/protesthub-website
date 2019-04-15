# Create your models here.
import datetime

from django.db import models
from django.utils import timezone


class Demo(models.Model):
    title = models.CharField(max_length=400)
    adress = models.CharField(max_length=400)
    starting_time = models.DateTimeField()
    ending_time = models.DateTimeField()
    organizer = models.CharField(max_length=200)
    description = models.TextField(max_length=15000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)
