from django.db import models
from django.utils import timezone
from datetime import date, timedelta

# Create your models here.
class TaskData(models.Model):
    name = models.CharField(max_length = 200)
    created_at = models.DateTimeField(default=timezone.now(), blank=True, null=True)

    @property
    def datebetween(self):
        curr_date = timezone.now().date()
        created_date = self.created_at.date() if self.created_at else None

        if created_date:
            return curr_date - created_date
        else:
            return None

