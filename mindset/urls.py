from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', mindset, name='mindset'),
    path('mindsetb', mindsetB, name='mindsetB'),





]
