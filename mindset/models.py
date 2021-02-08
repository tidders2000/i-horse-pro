from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Goals(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    outcome = models.CharField(max_length=100, blank=True, default='outcome')
    performance_goal_1 = models.CharField(
        max_length=100, blank=True, default="performance goal")
    performance_goal_2 = models.CharField(
        max_length=100, blank=True, default="performance goal")
    performance_goal_3 = models.CharField(
        max_length=100, blank=True, default="performance goal")
    process_goal_1 = models.CharField(
        max_length=100, blank=True, default='process goal')
    process_goal_2 = models.CharField(
        max_length=100, blank=True, default='process goal')
    process_goal_3 = models.CharField(
        max_length=100, blank=True, default='process goal')
    process_goal_4 = models.CharField(
        max_length=100, blank=True, default='process goal')


class Control(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    can_control = ArrayField(models.TextField())
    cannot_control = ArrayField(models.TextField())
