from django.db import models
from django.urls import reverse

class Task(models.Model):
    complete = models.BooleanField(default=False)
    description = models.CharField(max_length=256)
    time_estimate = models.IntegerField()
    due_date = models.DateTimeField()

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('organizer:detail', kwargs={'pk': self.pk})
