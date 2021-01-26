from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', competition, name='competition'),
    path('<int:pk>', comp_create, name='comp_create'),
    path('comp_edit/<int:pk>', comp_edit, name="comp_edit"),
    path('history/', history, name='history'),
    path('editentry/<int:pk>', editentry, name='editentry'),






]
