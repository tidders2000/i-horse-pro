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

import stripe

def success(request):

 membership= Profile.objects.get(pk=request.user.pk)
 status=membership.membership
 return render(request,'success.html',{'status':status})

def cancel(request):
     instance = Profile.objects.get(pk=request.user.pk)
     instance.membership ='Free'
     instance.save()
     return render(request,'cancel.html')
# Create your views here.

#stripe.api_key = settings.STRIPE_SECRET
# Create your views here.

def pro(request):
 
 instance = Profile.objects.get(pk=request.user.pk)
 instance.membership ='Pro'
 instance.save()
 price="price_1MgrHWEbBBCp0sSzN8zMkWgr"
 stripe.api_key = settings.STRIPE_SECRET_KEY
 
 if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
            checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price,  
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=domain + '/wizard/success/',
            cancel_url=domain + '/wizard/cancel/',
        )
 return redirect(checkout_session.url, code=303)

def competition(request):
 instance = Profile.objects.get(pk=request.user.pk)
 instance.membership ='Competition'
 instance.save()

 price="price_1MgrGnEbBBCp0sSzEVLCpIuA"
 stripe.api_key = settings.STRIPE_SECRET_KEY
 
 if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
            checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price,  
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=domain + '/wizard/success/',
            cancel_url=domain + '/wizard/cancel/',
        )
 return redirect(checkout_session.url, code=303)

def wizard(request):

    user = request.user
    disc = Disipline.objects.all()
    myselection = CustomImages.objects.filter(user=user)
    if request.method == "POST":
        log = wizard_form(
            request.POST, request.FILES)
        if log.is_valid():
            newlog = log.save(commit=False)
            newlog.user = user
            newlog.save()

    return render(request, 'wizard.html', {'disc': disc, 'myselection': myselection})


def deletedisipline(request, pk):
    item = get_object_or_404(CustomImages, pk=pk)
    item.delete()

    return redirect('wizard')


def addDisc(request, pk):
    dis = get_object_or_404(Disipline, pk=pk)
    user = request.user
    custimg = CustomImages(user=user, disipline=dis)
    custimg.save()

    return redirect('wizard')


@csrf_exempt
def select_img(request):
    user = request.user
    custimg = CustomImages.objects.filter(user=user)
    wizard_form()
    if request.method == "POST":
        pk = request.POST.get("pk")
        obj = get_object_or_404(CustomImages, pk=pk)
        obj.image = request.FILES.get("inputfile")
        obj.save()
        return redirect('select_img')

    return render(request, 'wizard_img.html', {'custimg': custimg, 'wizard_form': wizard_form})


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


@login_required()
def wizard_payment(request):
    user = request.user
    if request.method == "POST":

        return redirect('payment')

    return render(request, "wizard_payment.html", {})


def reset_wiz(request):
    instance = Profile.objects.get(pk=request.user.pk)
    instance.wizard = False
    instance.save()
    return redirect('home')


@login_required()
def payment(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            total = 0

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

                if customer.paid:
                    messages.error(request, "You have successfully paid")
                    request.session['cart'] = {}
                    return redirect(reverse('products'))
                else:
                    messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(
                request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        # 'publishable': settings.STRIPE_PUBLISHABLE

    return render(request, "payment.html", {'order_form': order_form, 'payment_form': payment_form})
