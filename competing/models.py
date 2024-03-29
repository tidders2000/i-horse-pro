from django.db import models
from training.models import CustomImages
from horse.models import Horse
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class CompetitionLog(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    date = models.DateTimeField(
        auto_now=False, null=True)
    disipline = models.CharField(max_length=100, blank=True)

    location = models.CharField(max_length=100, blank=True)
    lightbulb = models.CharField(max_length=100, blank=True)

    image = models.ImageField(
        upload_to='media/images/competition', blank=True, default='')
    performance = models.TextField(blank=True)
    myStars = models.CharField(max_length=100, blank=True)
    videoLink = models.CharField(max_length=100, blank=True)


class Venue(models.Model):
    venueName = models.CharField(max_length=100, blank=True)
    competition = models.ForeignKey(
        CompetitionLog, null=True, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, blank=True)
    refreshments = models.CharField(max_length=1, blank=True)
    prizes = models.CharField(max_length=1, blank=True)
    atmosphere = models.CharField(max_length=1, blank=True)

    def __str__(self):
        return self.venueName


class Comphorse(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    competition = models.ForeignKey(
        CompetitionLog, null=True, on_delete=models.CASCADE)
    horse = models.ForeignKey(Horse, null=True, on_delete=models.CASCADE)
    horseClass = models.CharField(max_length=100, blank=True)
    cost = models.TextField(blank=True)
    class_time = models.TimeField(auto_now=False,blank=True,default='12:00')
