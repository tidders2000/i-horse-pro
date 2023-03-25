from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
  
 
    path('wizard_paymment', wizard_payment, name='wizard_payment'),
 
    path('wizard_addhorse', wizard_addhorse, name='wizard_addhorse'),
 
    path('cancel',cancel,name="cancel"),
    path('success',success,name='success'),
    path('pro',pro,name='pro'),
    path('competition',competition,name='competitionmem'),
      path('cancelsub/', cancelsub, name='cancelsub'),





]
