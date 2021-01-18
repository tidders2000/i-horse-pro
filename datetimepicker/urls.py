from django.conf.urls import path

from .views import JSTemplateView


urlpatterns = [path('loader.js',
                    JSTemplateView.as_view(),
                    name='datetimepicker-loader')]
