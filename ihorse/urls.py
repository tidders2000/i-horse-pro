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
from home.views import ServiceWorkerView, fbsw
from accounts.views import index


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', include('home.urls')),
    path('training/', include('training.urls')),
    path('cal/', include('cal.urls')),
    path('mindset/', include('mindset.urls')),
    path('horse/', include('horse.urls')),
    path('appointment/', include('appointment.urls')),
    path('competing/', include('competing.urls')),
    path('sendpush/', include('sendpush.urls')),

    path(
        'sworker.js',
        ServiceWorkerView.as_view(),
        name='ServiceWorkerView',
    ),

    path(
        'firebase-messaging-sw.js',
        fbsw.as_view(),
        name='fbsw',
    ),
    path('webpush/', include('webpush.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),

]
