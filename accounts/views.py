from django.shortcuts import render, redirect, reverse,get_object_or_404
from django.http import HttpResponse  
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm
from .forms import ProfileForm
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .token import account_activation_token 
from django.core.mail import send_mail 
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from .models import *
from datetime import datetime
from datetime import date,timedelta
from django.conf import settings
from django.template.context_processors import csrf

from django.views.generic import TemplateView
import urllib.request


 # removes user
def deleteuser(request):

# user gets are you sure page 
    if request.method == 'POST':
        user=request.user
        user.delete()
        return redirect(reverse('home'))
    return render(request,'deleteacc.html')

#displays privacy policy
def pp(request): 

 return render(request,'privacypolicy.html')

#log user in
def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == 'POST':
       
        login_form = UserLoginForm(request.POST)
#authenticates user using standard model
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,
                                     password=password)

            if user is not None:
                auth.login(request=request, user=user)

                # instance = Profile.objects.get(pk=request.user.pk)
                messages.error(request, "You have successfully logged in")
              
                return redirect(reverse('home'))
            else:

                messages.error(request, "Sorry incorrect password/email")
                messages.error(request, user)
              

    else:
        login_form = UserLoginForm()

    
   

    return render(request,"login.html", {'login_form': login_form})


def index(request):
 
 
    if request.method == 'POST':
       
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,
                                     password=password)

            if user is not None:
                auth.login(request=request, user=user)
                instance = Profile.objects.get(pk=request.user.pk)
                messages.error(request, "You have successfully logged in")
            
                return redirect(reverse('home'))
            else:

                messages.error(request, "Sorry incorrect password/email")
                return render(request, 'index.html', {'login_form': login_form})
              

    else:
        login_form = UserLoginForm()
 
    return render(request, 'index.html', {'login_form': login_form})


def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect('index')

""" token for checking user has valid token and activating"""
def activate(request, uidb64, token):  
  
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        status='Thank you for your email confirmation. Now you can login to your account.'
        return render(request,'accaccount.html',{'status':status}) 
    else:  
         status='Activation link is invalid!'
         return render(request,'accaccount.html',{'status':status}) 
         

def registration(request):

  
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
      
        profile_form = ProfileForm(request.POST, request.FILES)
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if User.objects.filter(email=email).exists():
         messages.error(request, "Email Already In Use")
         return redirect(reverse('registration'))
        
        if password1 != password2:
         messages.error(request, "Passwords Do Not Match")
         return redirect(reverse('registration'))
      

     
  #auto create a profile where user details recide
        if registration_form.is_valid() :
          
          
            xe = registration_form.save()
            xe.profile.telephone = '000000000'
            xe.profile.membership = "Basic" # sets basic membership as standard
       

            xe.is_active = False # sets accouht inactive until activated from email token
            xe.save()
            user=xe
            #to get the domain of the current site  
            current_site = get_current_site(request)  
            #sets up message text to register user
            message = render_to_string('acc_active_email.html', {  
                'user': xe,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            }) 


            

          
                # sends email using sendgridgets user e mail
            to_email =  registration_form.cleaned_data.get('email') 
             # sends email using sendgrid
            send_mail('IHorse Account activation',message,'reg@ihorse.com',[to_email],html_message=message)
            #uses mail message template in templates
            return render(request,'mailmessage.html')
     
   
        

    registration_form = UserRegistrationForm()
    profile_form = ProfileForm()
    return render(request, 'registration.html', {'registration_form': registration_form, 'profile_form': profile_form})


@login_required
def user_profile(request):
     # sets up push notifications and displays user profile poage
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    user = request.user
    """the users profile page"""
    instance = get_object_or_404(Profile, user=user)
    if request.method == "POST":

        form = ProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save(commit=True)

        return redirect(reverse('home'))
      

    profile = ProfileForm(instance=instance)
    return render(request, 'profile.html', {'profile': profile, 'instance': instance, 'user': user, 'vapid_key': vapid_key})


# class ServiceWorkerView(TemplateView):
#     template_name = 'sw.js'
#     content_type = 'application/javascript'
#     name = 'sw.js'

 # default page is connection lost
def offline(request):
    return render(request, 'offline.html')

#form for users to register interest delete when app is liv e
def emailList(request):
    if request.method =="POST":
        fname=request.POST.get('fn')
        lname= request.POST.get('ln')
        email= request.POST.get('em')
        dis = request.POST.get('di')
        obj = Register_email.objects.create(fname=fname, lname=lname, dis=dis, email=email)
      
      
        obj.save()
        messages.success(request, "Thanks, Interest noted")

  



    return redirect(reverse('index'))

def help(request):
    return render(request, 'help.html')