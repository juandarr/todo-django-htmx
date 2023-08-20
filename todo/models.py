from django.db import models
from datetime import datetime
from django.utils.timezone import now

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150, null=True)
    complete = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=now, editable=False)