"""screenpop URL Configuration

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

from django.urls import path, include
from .views import *


urlpatterns = [
  
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('register/', registration, name='registration'),
    path('profile/', user_profile, name='profile'),
    path('emailList', emailList, name="emailList"),
    path('deleteuser', deleteuser, name="deleteuser"),
      path('help', help, name="help"),
 
    path('pp',pp,name='pp'),
    path('reset', include('password_reset.urls')),
    path('webpush/', include('webpush.urls')),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        activate, name='activate'),  
    # path('test', test, name='test'),
    # path(
    #     'sw.js',
    #     ServiceWorkerView.as_view(),
    #     name='ServiceWorkerView',



    # ),

]
