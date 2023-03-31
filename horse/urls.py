from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', horse, name='horse'),
    path('edithorse/<int:pk>', edithorse, name='edithorse'),
    path('deletehorse/<int:pk>', deletehorse, name='deletehorse'),
    path('photo/<int:pk>', photo, name='photo'),
    path('links/<int:pk>', links, name='links'),
    path('tackedit/<int:pk>', tackedit, name='tackedit'),
    path('details/', details, name='details'),
    path('details/<int:pk>', detailsInd, name='detailsInd'),
   
    path('deletetack/<int:pk>', deletetack, name='deletetack'),

    path('deletelink/<int:pk>', deletelink, name='deletelink'),
    path('savepassport/<int:pk>',savepassport,name="savepassport")




]
