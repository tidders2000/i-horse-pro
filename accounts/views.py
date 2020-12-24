from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm
from .forms import ProfileForm

from .models import Profile
from datetime import datetime
from datetime import date
from django.conf import settings
from django.template.context_processors import csrf

from django.views.generic import TemplateView


def login(request):
    """Return a login page"""

    return redirect('index')


def index(request):

    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,
                                     password=password)

            if user is not None:
                auth.login(request=request, user=user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('home'))
            else:

                messages.error(request, "oops")
                messages.error(request, user)
                # redirects to switcher instead of dash to set group and business

    else:
        login_form = UserLoginForm()

    return render(request, 'index.html', {'login_form': login_form})


def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect('index')


@login_required
def registration(request):

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        telephone = request.POST.get("telephone", "default")
        image = request.FILES.get("profile_image")

        if registration_form.is_valid() and profile_form.is_valid():
            xe = registration_form.save()
            xe.profile.telephone = telephone
            xe.profile.profile_image = image
            xe.save()
            return redirect(reverse('new_business'))

    registration_form = UserRegistrationForm()
    profile_form = ProfileForm()
    return render(request, 'registration.html', {'registration_form': registration_form, 'profile_form': profile_form})


@login_required
def user_profile(request):
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    user = request.user
    """the users profile page"""
    instance = Profile.objects.get(pk=request.user.pk)
    if request.method == "POST":

        form = ProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save(commit=True)

        return redirect(reverse('home'))
        messages.error(request, "Profile Updated")

    profile = ProfileForm(instance=instance)
    return render(request, 'profile.html', {'profile': profile, 'instance': instance, 'user': user, 'vapid_key': vapid_key})


# class ServiceWorkerView(TemplateView):
#     template_name = 'sw.js'
#     content_type = 'application/javascript'
#     name = 'sw.js'


def error(request):
    return render(request, 'error.html')
