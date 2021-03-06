from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Goals(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=100, blank=True, default="Title")
    outcome = models.TextField(max_length=256, blank=True, default='outcome')
    performance_goal_1 = models.TextField(
        max_length=256, blank=True, default='Performance Goal')
    performance_goal_2 = models.TextField(
        max_length=256, blank=True, default='Performance Goal')
    performance_goal_3 = models.TextField(
        max_length=256, blank=True, default='Performance Goal')
    process_goal_1 = models.TextField(
        max_length=256, blank=True, default='Process Goal')
    process_goal_2 = models.TextField(
        max_length=256, blank=True, default='Process Goal')
    process_goal_3 = models.TextField(
        max_length=256, blank=True, default='Process Goal')
    process_goal_4 = models.TextField(
        max_length=256, blank=True, default='Process Goal')


class Control(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    can_control = ArrayField(models.TextField())
    cannot_control = ArrayField(models.TextField())
