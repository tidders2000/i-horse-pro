"""ihorse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import ServiceWorkerView, fbsw, sw
from accounts.views import index, offline




urlpatterns = [
    path('', index, name='index'),
    path('offline.html', offline, name='offline'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', include('home.urls')),
    path('wizard/', include('wizard.urls')),
    path('training/', include('training.urls')),
    path('cal/', include('cal.urls')),
   
    path('horse/', include('horse.urls')),
    path('appointment/', include('appointment.urls')),
    path('competing/', include('competing.urls')),
    path('yard/', include('yard.urls')),
    path('sendpush/', include('sendpush.urls')),
    path('webpush/', include('webpush.urls')),
    path(
        'sworker.js',
        ServiceWorkerView.as_view(),
        name='ServiceWorkerView',
    ),

       path(
        'sw.js',
        sw.as_view(),
        name='sw',
    ),

    path(
        'firebase-messaging-sw.js',
        fbsw.as_view(),
        name='fbsw',
    ),
   
    path('ratings/', include('star_ratings.urls', namespace='ratings')),

]
