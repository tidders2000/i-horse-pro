from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def home(request):

    return render(request, 'home.html')


class ServiceWorkerView(TemplateView):
    template_name = 'sworker.js'
    content_type = 'application/javascript'
    name = 'sw.js'


def error(request):
    return render(request, 'error.html')
