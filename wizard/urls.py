from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', wizard, name='wizard'),
    path('select_img', select_img, name='select_img'),
    path('wizard_paymment', wizard_payment, name='wizard_payment'),
    path('payment', payment, name='payment'),
    path('reset', reset_wiz, name='reset_wiz'),
    path('wizard_addhorse', wizard_addhorse, name='wizard_addhorse'),
    path('<int:pk>', addDisc, name='addDisc'),
    path('deletedisipline/<int:pk>', deletedisipline, name="deletedisipline"),
    path('cancel',cancel,name="cancel"),
    path('success',success,name='success'),
    path('pro',pro,name='pro'),
    path('competition',competition,name='competitionmem')





]
