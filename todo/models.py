from django.db import models
from datetime import datetime
from django.utils.timezone import now

class Todo(models.Model):
    description = models.CharField(max_length=120)
    complete = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=now, editable=False)