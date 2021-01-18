from django.db import models
from horse.models import Horse


from django.contrib.auth.models import User


class Event(models.Model):
    appType = models.CharField(max_length=100)

    def __str__(self):
        return self.appType


class Appointment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    horse = models.ForeignKey(Horse, null=True, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    due = models.DateTimeField(
        auto_now=False, null=True)
    end = models.DateTimeField(
        auto_now=False, blank=True)

    report = models.ImageField(
        upload_to='media/images/appoint', blank=True)
    notes = models.TextField(blank=True)

# Create your models here.
