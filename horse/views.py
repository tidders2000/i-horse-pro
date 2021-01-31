from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .forms import horse_form, link_form, tack_form
from django.contrib import messages
from .models import *
from appointment.models import Appointment
from training.models import TrainingLog

# Create your views here.


def horse(request):

    user = request.user
    form = horse_form()
    if request.method == "POST":
        horsef = horse_form(request.POST)
        if horsef.is_valid():
            horseSave = horsef.save(commit=False)
            horseSave.user = user
            horseSave.save()
            request.session['horse'] = horseSave.pk
            return redirect(reverse('photo'))
        # messages.error(request, 'Horse added')

    return render(request, 'horse.html', {'form': form})


def photo(request):
    horse = request.session['horse']
    newHorse = Horse.objects.get(pk=horse)
    if request.method == "POST":
        photo = request.FILES.get('pic')

        newHorse.photo = photo
        newHorse.save()
        return redirect(reverse('tackhorse', kwargs={'pk': horse}))

    return render(request, 'photo.html', {'horse': horse, 'newHorse': newHorse})


def tack(request):
    horse = request.session['horse']
    display = 'none'  # hides back button only visible on edit
    user = request.user
    newHorse = Horse.objects.get(pk=horse)
    tack = tack_form()
    tackdetails = Tack.objects.all().filter(horse=newHorse)
    if request.method == "POST" and 'link' in request:
        tackf = tack_form(request.POST)
        if tackf.is_valid():
            tackSave = tackf.save(commit=False)
            tackSave.user = user
            tackSave.horse = newHorse
            tackSave.save()
    return render(request, 'tack.html', {'tack': tack, 'tackdetails': tackdetails, 'horse': horse, 'display': display})


def tackhorse(request, pk):

    user = request.user
    display = "inline"  # only visible on edit screen css for back button
    horse = Horse.objects.get(pk=pk)
    tack = tack_form()
    tackdetails = Tack.objects.all().filter(horse=horse)
    if request.method == "POST":
        tackf = tack_form(request.POST)
        if tackf.is_valid():
            tackSave = tackf.save(commit=False)
            tackSave.user = user
            tackSave.horse = horse
            tackSave.save()
    return render(request, 'tack.html', {'tack': tack, 'tackdetails': tackdetails, 'horse': horse, 'display': display})


def links(request):
    horse = request.session['horse']
    user = request.user
    newHorse = Horse.objects.get(pk=horse)
    link = link_form()
    links = Link.objects.all().filter(horse=newHorse)
    if request.method == "POST":
        linkf = link_form(request.POST)
        if linkf.is_valid():
            linkSave = linkf.save(commit=False)
            linkSave.user = user
            linkSave.horse = newHorse
            linkSave.save()
    return render(request, 'links.html', {'link': link, 'links': links, 'horse': horse})


def details(request):
    user = request.user
    horses = Horse.objects.all().filter(user=user)
    return render(request, 'horse_details.html', {'horses': horses})


def detailsInd(request, pk):
    user = request.user
    string = request.session['history']
    if request.session['history']:

        tory = Appointment.objects.all().filter(event__appType=string)

    else:
        tory = Appointment.objects.all().filter(event__appType="Dentist")
        request.session['history'] = "Dentist"
        string = request.session['history']

    horses = Horse.objects.all().filter(user=user)
    training = TrainingLog.objects.all().filter(horse=pk).order_by('-date')[:5]
    links = Link.objects.all().filter(horse=pk)
    selected = Horse.objects.get(pk=pk)
    appointments = Appointment.objects.all().filter(
        horse=selected).order_by('event__appType', '-due')
    appointments = appointments.distinct('event__appType')

    if request.method == "POST":
        if 'save_obj' in request.POST:
            photo = request.FILES.get('pic')
            selected.passport = photo
            selected.save()

        if 'apps' in request.POST:

            request.session['history'] = request.POST.get('apps')
            print(request.POST.get('type'))
            return redirect(reverse('detailsInd', kwargs={'pk': pk}) + '#apps')

    return render(request, 'horse_details_ind.html', {'tory': tory, 'training': training, 'appointments': appointments, 'selected': selected, 'horses': horses, 'links': links})
