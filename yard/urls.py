from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', yard_menu, name='yard_menu'),
    path('people/', people, name='people'),
    path('staff/', staff, name='staff'),
    path('edit_staff/<int:pk>/', edit_staff, name='edit_staff'),
    path('clients/', clients, name='clients'),
    path('edit_client/<int:pk>/', edit_client, name='edit_client'),
    path('delete_client/<int:pk>', delete_client, name='delete_client'),
    path('delete_staff/<int:pk>', delete_staff, name='delete_staff'),
]
