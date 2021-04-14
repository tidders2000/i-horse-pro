from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name='home'),

    path(
        'sworker.js',
        ServiceWorkerView.as_view(),
        name='ServiceWorkerView',
    ),



]
