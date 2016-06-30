from __future__ import unicode_literals
from django.db import models
from datetime import datetime, date, time

class Task(models.Model):
             
    name = models.CharField(max_length=100)
    due = models.DateTimeField()
    complete = models.BooleanField(default=False)

    # if complete is false, datetime_completed will be None
    datetime_completed = models.DateTimeField(null=True, blank=True, default=None)
          

    def __unicode__(self):
        return self.name


    def __str__(self):
        return self.name

    def pastDue(self):
        if self.complete:
            return False
        return datetime.now() > self.due


    # return true if this task is due in less than twelve hours
    def dueSoon(self):
        TWELVE_HOURS = 60 * 60 * 12

        if self.pastDue() or self.complete:
            return False
        
        # check total difference between due and now
        delta = self.due - datetime.now()
        if delta.days > 1:
            return False
        if delta.total_seconds() < TWELVE_HOURS:
            return True
        return False
