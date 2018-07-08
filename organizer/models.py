from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

def no_past(value):
    today = timezone.now()
    if value < today:
        raise ValidationError('Date & time cannot be in the past.')


class Task(models.Model):
    complete = models.BooleanField(default=False)
    description = models.CharField(max_length=256)
    time_estimate = models.IntegerField(validators=[MinValueValidator(0)])
    due_date = models.DateTimeField(validators=[no_past])

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('organizer:detail', kwargs={'pk': self.pk})
