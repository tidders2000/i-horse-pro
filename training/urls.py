from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', training_log, name='training_log'),
    path('<int:pk>', training_create, name='training_create'),
    path('training_edit/<int:pk>', training_edit)





]
