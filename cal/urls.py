from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', cal, name='cal'),
    path('caltwo', calTwo, name='caltwo'),



]
