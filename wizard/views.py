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
     
   
        stripe.api_key = settings.STRIPE_SECRET_KEY
        instance = get_object_or_404(Profile, user=user)
        #try instance delete

        stripe.api_key = settings.STRIPE_SECRET_KEY
   
        subscription=stripe.Subscription.retrieve(instance.subId)
        print(subscription.current_period_end)
        renewal=subscription.current_period_end
        #sets unix date to string
        newDate=(datetime.datetime.utcfromtimestamp(renewal).strftime('%Y-%m-%d'))

# #sets date to delete sub in profile model
        instance.periodEnd = newDate
        instance.save()
        return redirect(reverse('home'))



       return render(request,'cancelsub.html')


       #payment sucess page for subscription

def success(request):
 user = request.user  
 instance = get_object_or_404(Profile, user=user)
 st=stripe.Subscription.list(limit=1)
 
 sub=st.data[0].id
 instance.subId=sub
 instance.save()
 status=instance.membership
 return render(request,'success.html',{'status':status})

#payment faliure page error handling to add
def cancel(request):
     user = request.user
     instance = get_object_or_404(Profile, user=user)
     instance.membership ='Free'
     instance.save()
     return render(request,'cancel.html')


#subscription for pro with stripe seperate functioun due to different variables

def pro(request):
 user = request.user
 instance = get_object_or_404(Profile, user=user)
 if instance.membership == 'Competition':
     messages.error(request,'Please cancel your Competing membership then upgrade')
       
     return redirect(reverse('home'))
 instance.membership ='Pro'
 instance.periodEnd=None
 instance.save()
 price="price_1MgrHWEbBBCp0sSzN8zMkWgr"
 stripe.api_key = settings.STRIPE_SECRET_KEY
 
 if settings.DEBUG:
     #add live site url
            # domain = 'http://127.0.0.1:8000'
            #switch when using development
<<<<<<< HEAD
            # domain = "https://i-horse-development-wmfrestkvv.herokuapp.com/"
            domain="https://i-horse.herokuapp.com/"
=======
#             domain = "https://i-horse-development-wmfrestkvv.herokuapp.com/"
# >>>>>>> c56f3445e841ff6345cce766d1257ca011d05934
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
 user = request.user
 instance = get_object_or_404(Profile, user=user)
  
 instance.periodEnd=None
 instance.membership ='Competition'
 instance.save()

 price="price_1MgrGnEbBBCp0sSzEVLCpIuA"
 stripe.api_key = settings.STRIPE_SECRET_KEY
 
 if settings.DEBUG:
          #add live site url
            # domain = 'http://127.0.0.1:8000'
 
<<<<<<< HEAD
            # domain = "https://i-horse-development-wmfrestkvv.herokuapp.com"

            domain="https://i-horse.herokuapp.com/"
=======
            domain = "https://i-horse-development-wmfrestkvv.herokuapp.com"
>>>>>>> c56f3445e841ff6345cce766d1257ca011d05934
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











