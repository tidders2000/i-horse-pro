from django.db import models
from django.contrib.auth.models import User
from horse.models import Horse
# Create your models here.

disipline = [('Dressage', 'Dressage'), ('ShowJumping', 'ShowJumping'),
             ('XC', 'XC'), ('PonyClub', 'PonyClub')]

user = User.username

# temp fix for setup wizard


class Disipline(models.Model):
    disipline = models.CharField(
        max_length=100, blank=True)

    def __str__(self):
        return self.disipline


class CustomImages(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    disipline = models.CharField(
        max_length=100, blank=True)
    image = models.ImageField(
        upload_to='media/images/custom', blank=True, default='media/images/200x300.png')

    def __str__(self):
        return self.disipline


class TrainingLog(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    horse = models.ForeignKey(
        Horse, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(
        auto_now=False, null=True)
    disipline = models.CharField(max_length=100, blank=True)
    instructor = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    lightbulb = models.CharField(max_length=100, blank=True)
    littlewins1 = models.CharField(max_length=100, blank=True)
    littlewins2 = models.CharField(max_length=100, blank=True)
    littlewins3 = models.CharField(max_length=100, blank=True)
    floorPlan = models.ImageField(
        upload_to='media/images/floorplan', blank=True, default='media/images/floor_plan.jpg')
    homework = models.TextField(blank=True)
    files = models.FileField(upload_to='media/uploads', blank=True)


class Objectives(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    session = models.ForeignKey(
        TrainingLog, null=True, on_delete=models.CASCADE)
    objective = models.CharField(max_length=100, blank=True)
    Completed = models.BooleanField()
