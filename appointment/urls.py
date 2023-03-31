from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('<int:pk>', appointment, name='appointment'),
    path('feed.ics$/feed.ics$/<int:pk>', EventFeed(), name='EventFeed'),
    path('edit/', editapp, name='editapp'),
    # path('ical/', ical, name='ical')
    path('get_csrftoken_from_cookie', get_csrftoken_from_cookie,
     name='get_csrftoken_from_cookie'),

    path('deleteAppointment/<int:pk>',deleteAppointment,name='deleteAppointment')


]
