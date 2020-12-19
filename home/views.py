from django.shortcuts import render
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification
import json
from django.views.generic import TemplateView


# Create your views here.


def home(request):
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    user = request.user

    return render(request, 'home.html', {user: user, 'vapid_key': vapid_key})


class ServiceWorkerView(TemplateView):
    template_name = 'sworker.js'
    content_type = 'application/javascript'
    name = 'sw.js'


def error(request):
    return render(request, 'error.html')
