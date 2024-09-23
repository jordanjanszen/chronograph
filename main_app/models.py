from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField(max_length=250)
    category = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.now)
    comment = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('events_detail', kwargs={'event_id': self.id})