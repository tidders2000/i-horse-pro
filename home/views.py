# from asyncio.windows_events import NULL
from operator import is_not
from django.shortcuts import render,redirect, reverse
from django.db.models import Q
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
from horse.models import Horse,Images_new
from appointment.models import Appointment
from competing.models import CompetitionLog
from training.models import TrainingLog
from django.contrib import messages
from datetime import datetime
from datetime import date
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
import stripe
from django.conf import settings

# Create your views here.

@login_required
def home(request):
    # webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    # vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
  



    user = request.user
    """the users profile page"""
    instance = Profile.objects.get(pk=request.user.pk)
    # if request.user.is_authenticated:
    #     if instance.wizard == True:
    #                 print("True")
    #                 return redirect(reverse('wizard_payment'))
    
 

  

  
    now = datetime.now().date()
  

    #checks that subscription cancel date has not passed and if so converts to free membership in profile
    if instance.periodEnd:
        if instance.periodEnd < now:
            #deletes subscriuption from strip[e using key in model subid
                stripe.api_key = settings.STRIPE_SECRET_KEY
                stripe.Subscription.delete(instance.subID)
        #resets sub to free
                instance.membership ='Free'
                instance.save()
        else:
            x=instance.periodEnd.strftime("%d/%m/%Y")# converts unix date to string and tells user expiry
            messages.error(request, "Your membership expires on "+x)
            
  #checks user memebership and limits query results to allocates number of horses

    if user.profile.membership=="Free":
     horses = Horse.objects.all().filter(user=user)[:1]
    elif  user.profile.membership=="Competition":
         horses = Horse.objects.all().filter(user=user)[:5]
    else:
         horses = Horse.objects.all().filter(user=user)[:10]

    #data for home page such as appointments and competitons
    events = Appointment.objects.all().filter(Q(user=user,due__gte=now)).order_by('due')[:6]
    comps = CompetitionLog.objects.all().filter(
        user=user,date__gte=now).order_by('date')[:6]
   

    training = TrainingLog.objects.all().filter(
        user=user,date__gte=now).order_by('date')[:6]
    train_his = TrainingLog.objects.all().filter(user=user, date__lte=now).order_by('-date')[:6]
    comp_his = CompetitionLog.objects.all().filter(user=user, date__lte=now).order_by('-date')[:6]
    request.session['history'] = "Dentist"  # sets appointments for horse links
    request.session['dis'] = 'none'  # sets appointment display css

    return render(request, 'home.html', {'horses': horses, 'events': events, 'comps': comps, 'training': training,'train_his':train_his,'comp_his':comp_his})


@require_POST
@csrf_exempt
def save_info(request):

    return HttpResponse(status=400)

#loads service worler for offline
class ServiceWorkerView(TemplateView):
    template_name = 'sworker.js'
    content_type = 'application/javascript'
    name = 'sworker.js'

class sw(TemplateView):
    template_name = 'sw.js'
    content_type = 'application/javascript'
    name = 'sw.js'

#loads sw for notifcation messaging  via firebase
class fbsw(TemplateView):
    template_name = 'firebase-messaging-sw.js'
    content_type = 'application/javascript'
    name = 'firebase-messaging-sw.js'

#error view

def error(request):
    return render(request, 'error.html')
