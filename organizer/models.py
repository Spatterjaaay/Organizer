from django.db import models

class TodoItem(models.Model):
    complete = models.BooleanField()
    description = models.CharField(max_length=256)
    time_estimate = models.IntegerField()
    due_date = models.DateTimeField()
