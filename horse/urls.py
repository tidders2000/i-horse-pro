from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', horse, name='horse'),
    path('photo/', photo, name='photo'),
    path('links/', links, name='links'),
    path('tackedit/<int:pk>', tackedit, name='tackedit'),
    path('details/', details, name='details'),
    path('details/<int:pk>', detailsInd, name='detailsInd'),
    path('tack/<int:pk>', tackhorse, name='tackhorse'),
    path('deletetack/<int:pk>', deletetack, name='deletetack')




]
