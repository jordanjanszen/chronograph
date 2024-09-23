from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField(max_length=250)
    category = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.now)
    comment = models.TextField(max_length=250)

    def __str__(self):
        return self.name