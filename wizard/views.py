from django.shortcuts import render, get_object_or_404, redirect, reverse
from training.models import CustomImages, Disipline
from training.forms import wizard_form
from horse.forms import wizard_horse_form
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from accounts.models import Profile
import datetime


import stripe

#cancel users subscription

def cancelsub(request):
       
       if request.method == 'POST':
        user=request.user
        user.delete()
   
        stripe.api_key = settings.STRIPE_SECRET_KEY
        instance = Profile.objects.get(pk=request.user.pk)
        subscription=stripe.Subscription.retrieve(instance.subId)
        renewal=subscription.current_period_end
        #sets unix date to string
        newDate=(datetime.datetime.utcfromtimestamp(renewal).strftime('%Y-%m-%d'))

#sets date to delete sub in profile model
        instance.periodEnd = newDate
        instance.save()
        return redirect(reverse('home'))



       return render(request,'cancelsub.html')


       #payment sucess page for subscription

def success(request):
 st=stripe.Subscription.list(limit=1)
 membership= Profile.objects.get(pk=request.user.pk)
 sub=st.data[0].id
 membership.subId=sub
 membership.save()
 status=membership.membership
 return render(request,'success.html',{'status':status})

#payment faliure page error handling to add
def cancel(request):
     instance = Profile.objects.get(pk=request.user.pk)
     instance.membership ='Free'
     instance.save()
     return render(request,'cancel.html')


#subscription for pro with stripe seperate functioun due to different variables

def pro(request):
 
 instance = Profile.objects.get(pk=request.user.pk)
 instance.membership ='Pro'
 instance.save()
 price="price_1MgrHWEbBBCp0sSzN8zMkWgr"
 stripe.api_key = settings.STRIPE_SECRET_KEY
 
 if settings.DEBUG:
     #add live site url
            # domain = 'http://127.0.0.1:8000'
            #switch when using development
            domain = "https://i-horse-development-wmfrestkvv.herokuapp.com/"
            checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price,  
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=domain + '/wizard/success',
            cancel_url=domain + '/wizard/cancel',
            )
            
 return redirect(checkout_session.url, code=303)
#competition membership with stripe
def competition(request):
 instance = Profile.objects.get(pk=request.user.pk)
 instance.membership ='Competition'
 instance.save()

 price="price_1MgrGnEbBBCp0sSzEVLCpIuA"
 stripe.api_key = settings.STRIPE_SECRET_KEY
 
 if settings.DEBUG:
          #add live site url
      # "https://i-horse-development-fezeitgzxk.herokuapp.com"
            domain = "https://i-horse-development-wmfrestkvv.herokuapp.com/"
            checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price,  
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=domain + '/wizard/success',
            cancel_url=domain + '/wizard/cancel',
        )
 return redirect(checkout_session.url, code=303)
 
#render subscription options

@login_required()
def wizard_payment(request):
    user = request.user
    if request.method == "POST":

        return redirect('payment')

    return render(request, "wizard_payment.html", {})



#allows add horse when log for first time not in current use


def wizard_addhorse(request):
    form = wizard_horse_form()
    user = request.user
    if request.method == "POST":
        hors = wizard_horse_form(
            request.POST, request.FILES)
        if hors.is_valid():
            newlog = hors.save(commit=False)
            newlog.user = user
            newlog.save()
            pic = newlog.photo
            messages.error(request, "Horse Added")
            return redirect('wizard_payment')

    return render(request, 'wizard_addhorse.html', {'form': form})











