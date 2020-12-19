"""webpushdjango URL Configuration
...
"""
from django.contrib import admin
from django.urls import path, include

from .views import home, send_push

urlpatterns = [

    path('', home),

    path('sendpush/', send_push),
    path('webpush/', include('webpush.urls')),
]
