from django.shortcuts import render

from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification
import json
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET


# Create your views here.


def home(request):
    # webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    # vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    # user = request.user

    return render(request, 'home.html')


@require_POST
@csrf_exempt
def save_info(request):

    return HttpResponse(status=400)


class ServiceWorkerView(TemplateView):
    template_name = 'sworker.js'
    content_type = 'application/javascript'
    name = 'sworker.js'


class fbsw(TemplateView):
    template_name = 'firebase-messaging-sw.js'
    content_type = 'application/javascript'
    name = 'firebase-messaging-sw.js'


def error(request):
    return render(request, 'error.html')
