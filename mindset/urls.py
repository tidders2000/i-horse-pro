from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', mindset_select, name='mindset_select'),
    path('mindsetb', mindsetB, name='mindsetB'),
    path('mindset/<int:pk>', mindset, name='mindset'),
    path('title_add', title_add, name='title_add'),
    path('delete_goal/<int:pk>', delete_goal, name="delete_goal")




]
