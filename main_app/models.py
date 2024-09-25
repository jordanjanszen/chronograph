from django.db import models
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Unique name for the category
    color = models.CharField(max_length=7, default='#FFFFFF')  # Color in hex format
    features = models.TextField(blank=True)  # List of features (could be a description)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Unique name for the tag

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')  # Foreign key to Category
    start_date = models.DateField(default=timezone.now)  # Start date
    end_date = models.DateField(null=True, blank=True)  # End date
    start_time = models.TimeField(null=True)  # Start time
    end_time = models.TimeField(null=True)  # End time
    duration = models.DurationField(null=True, blank=True)  # Duration
    tags = models.ManyToManyField(Tag, blank=True)  # Many-to-many relationship with Tag
    comment = models.TextField(max_length=250, blank=True)  # Optional comment
    description = models.TextField(blank=True)  # Additional details
    is_done = models.BooleanField(default=False)  # Done status
    created_at = models.DateTimeField(auto_now_add=True)  # Creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Update timestamp
    recurrence = models.CharField(max_length=50, blank=True)  # Recurrence

    def __str__(self):
        return f'{self.name} ({self.start_date} - {self.end_date}){self.id}'

    def get_absolute_url(self):
        return reverse('events_detail', kwargs={'event_id': self.id})
