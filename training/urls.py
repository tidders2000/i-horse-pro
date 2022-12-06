from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', training_log, name='training_log'),
    path('<int:pk>', training_create, name='training_create'),
    path('training_edit/<int:pk>', training_edit, name="training_edit"),
    path('checkOb/<int:pk>', checkOb, name="checkOb"),
    path('feed.ics$', EventFeed3(), name='EventFeed3'),
    path('draw/<int:pk>', draw, name='draw'),
    path('savedraw/<int:pk>', savedraw, name="savedraw"),
    path('deleteobjective/<int:pk>',deleteobjective, name='deleteobjective')





]
