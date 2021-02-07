from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', wizard, name='wizard'),
    path('deletedisipline/<int:pk>', deletedisipline, name="deletedisipline")




]
