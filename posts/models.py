from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    Important = 'Important'
    Very_Important = 'Very Important'
    Not_So_Important = 'Not So Important'
    priority_choices = [(Important, 'Important'), (Very_Important, 'Very Important'),
                        (Not_So_Important, 'Not So Important')]
    description = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default='New Task')
    due_date = models.DateField(auto_now=False, default=timezone.now)
    due_time = models.TimeField(auto_now=False, default=timezone.now)
    priority = models.CharField(max_length=18, choices=priority_choices, default=Important)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title