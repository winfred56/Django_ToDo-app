from django.db import models
from django.utils import timezone

class Post(models.Model):
    Important = 'Important'
    Very_Important = 'Very Important'
    Not_So_Important = 'Not So Important'
    priority_choices = [(Important, 'Important'),(Very_Important,'Very Important'),(Not_So_Important,'Not So Important')]
    description = models.TextField()
    title = models.CharField(max_length=50, default='New')
    due_date = models.DateField(auto_now=False, default=timezone.now)
    due_time = models.TimeField(auto_now=False, default=timezone.now )
    priority = models.CharField(max_length=18, choices=priority_choices, default=Important)
    done = models.BooleanField()
