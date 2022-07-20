from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404
from .forms import horse_form, link_form, tack_form
from django.contrib import messages
from .models import *
from appointment.models import Appointment
from training.models import TrainingLog
from datetime import datetime, timedelta, time

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
            messages.error(request, "Horse Saved")
            return redirect(reverse('detailsInd', kwargs={'pk':horseSave.pk}))
            # return redirect(reverse('photo'))
        # messages.error(request, 'Horse added')

    return render(request, 'horse.html', {'form': form})


def photo(request,pk):
    selected = Horse.objects.get(pk=pk)
  
    if request.method == "POST":
            photo = request.FILES.get('pic')
           
            selected.photo = photo
            selected.save()
         
            messages.error(request, "photo Saved")  


     
    return redirect(reverse('detailsInd', kwargs={'pk': pk}))

def deletetack(request, pk):
    tackItem = get_object_or_404(Tack, pk=pk)
    horse = tackItem.horse.pk
    tackItem.delete()

    return redirect('tackedit', pk=horse)

def deletetackHorse(request, pk):
    tackItem = get_object_or_404(Tack, pk=pk)
    horse = tackItem.horse.pk
    tackItem.delete()

    return redirect('tackhorse', pk=horse)

def deletelink(request, pk):
    linkItem = get_object_or_404(Link, pk=pk)
    horse = linkItem.horse.pk
    linkItem.delete()

    return redirect('links', pk=horse)


def tackedit(request, pk):
    horse = get_object_or_404(Horse, pk=pk)
    tackdetails = Tack.objects.all().filter(horse=horse)
    user = request.user
    request.session['horse'] = pk
    tack = tack_form()

    if request.method == "POST":
        tackf = tack_form(request.POST)
        if tackf.is_valid():
            tackSave = tackf.save(commit=False)
            tackSave.user = user
            tackSave.horse = horse
            tackSave.save()
            messages.error(request, "Tack Saved")
            
    return render(request, 'tackedit.html', {'horse': horse, 'tack': tack, 'tackdetails': tackdetails, 'horse': horse})


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
            messages.error(request, "Tack Saved")
    return render(request, 'tack.html', {'tack': tack, 'tackdetails': tackdetails, 'horse': horse, 'display': display})


def links(request,pk):
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
            messages.error(request, "Link Saved")
    return render(request, 'links.html', {'link': link, 'links': links, 'horse': newHorse})


def details(request):
    user = request.user
    request.session['history'] = "Dentist"
    horses = Horse.objects.all().filter(user=user)
    return render(request, 'horse_details.html', {'horses': horses})


def detailsInd(request, pk):
    today = datetime.now().date()

    user = request.user
    string = request.session['history']
    selected = Horse.objects.get(pk=pk)
    if request.session['history']:

        tory = Appointment.objects.all().filter(event__appType=string).filter(
            horse=selected)

    else:
        tory = Appointment.objects.all().filter(event__appType="Dentist").filter(
            horse=selected)

        request.session['history'] = "Dentist"
        string = request.session['history']

    horses = Horse.objects.all().filter(user=user)
    training = TrainingLog.objects.all().filter(horse=pk).order_by('-date')[:5]
    links = Link.objects.all().filter(horse=pk)

    appointments = Appointment.objects.all().filter(
        horse=selected).order_by('event__appType', 'due')
    # appointments = appointments.distinct('event__appType')

    # if request.method == "POST":
       
    #     if 'save_pp' in request.POST:
           
    #         photo = request.FILES.get('pic')
    #         print(request.POST)
    #         selected.passport = photo
    #         selected.save()
         
    #         messages.error(request, "passport Saved")  

    if 'apps' in request.POST:

            request.session['history'] = request.POST.get('apps')

            return redirect(reverse('detailsInd', kwargs={'pk': pk}) + '#apps')
        
      

    return render(request, 'horse_details_ind.html', {'tory': tory, 'training': training, 'appointments': appointments, 'selected': selected, 'horses': horses, 'links': links})


def edithorse(request, pk):
    instance = get_object_or_404(Horse, pk=pk)
    form = horse_form(instance=instance)
    pk = pk
    user = request.user
    if request.method == "POST":
        request.session['horse'] = pk
        horsef = horse_form(request.POST, instance=instance)
        if horsef.is_valid():
            horsef.save()
            messages.error(request, "Horse Updated")
            # return redirect('photo')
            return redirect(reverse('detailsInd', kwargs={'pk': pk}))
    return render(request, 'horse_edit.html', {'form': form, 'pk': pk})


def deletehorse(request, pk):
    instance = get_object_or_404(Horse, pk=pk)
    instance.delete()
    messages.error(request, "Horse Deleted")

    return redirect(reverse('home'))


def savepassport(request,pk):
    selected = Horse.objects.get(pk=pk)
  
    if request.method == "POST":
            photo = request.FILES.get('pass')
           
            selected.passport = photo
            selected.save()
         
            messages.error(request, "passport Saved")  


     
    return redirect(reverse('detailsInd', kwargs={'pk': pk}))