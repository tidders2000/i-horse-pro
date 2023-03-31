from itertools import count
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404
from django.http import JsonResponse
from .forms import horse_form, link_form, tack_form
from django.contrib import messages
from .models import *
from appointment.models import Appointment
from training.models import TrainingLog
from datetime import datetime, timedelta, time
from django.db import connections
import random

#shows the horses

def horse(request):
    user = request.user
    horses = Horse.objects.all().filter(user=user).count()
#limits the horses shown in case membership decreased
    if user.profile.membership=="Free" and horses >=1:
         messages.error(request, 'Maximum reached') 
         return redirect('home')
    if user.profile.membership=="Competition" and horses >=3:
          messages.error(request, 'Maximum reached') 
          return redirect('home')

#save horse form 
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

#save photo
def photo(request,pk):
    
    selected = Horse.objects.get(pk=pk)
    #random number for unique id
    rand=random.randint(1,10000)
   
    if request.method == "POST":
            photo = request.FILES.get('id_image')
           
            selected.photo = photo
            selected.save()
            obj=Images_new.objects.create(photo=photo,horse=selected,id=rand)
         
            messages.error(request, "photo Saved")  

            return JsonResponse({'data':'Data uploaded'})
           
           
          


     
    return redirect(reverse('detailsInd', kwargs={'pk': pk}))

#delete tack

def deletetack(request, pk):
    tackItem = get_object_or_404(Tack, pk=pk)
    horse = tackItem.horse.pk
    tackItem.delete()

    return redirect('tackedit', pk=horse)

#delete link

def deletelink(request, pk):
    linkItem = get_object_or_404(Link, pk=pk)
    horse = linkItem.horse.pk
    linkItem.delete()

    return redirect('links', pk=horse)

#lists tack and add form
def tackedit(request, pk):
    horse = get_object_or_404(Horse, pk=pk)
    tackdetails = Tack.objects.all().filter(horse=horse)
    user = request.user
    request.session['horse'] = pk
    tack = tack_form()
#add tack
    if request.method == "POST":
        tackf = tack_form(request.POST)
        if tackf.is_valid():
            tackSave = tackf.save(commit=False)
            tackSave.user = user
            tackSave.horse = horse
            tackSave.save()
            messages.error(request, "Tack Saved")
            
    return render(request, 'tackedit.html', {'horse': horse, 'tack': tack, 'tackdetails': tackdetails, 'horse': horse})




#lists links to horse realted websites
def links(request,pk):
    horse = request.session['horse']
    user = request.user
    newHorse = Horse.objects.get(pk=horse)
    link = link_form()
    links = Link.objects.all().filter(horse=newHorse)
    #add links form
    if request.method == "POST":
        linkf = link_form(request.POST)

        if linkf.is_valid():
            linkSave = linkf.save(commit=False)
            linkSave.user = user
            linkSave.horse = newHorse
            linkSave.save()
            messages.error(request, "Link Saved")
    return render(request, 'links.html', {'link': link, 'links': links, 'horse': newHorse})

#displays list of users horses
def details(request):
    user = request.user
   
    if user.profile.membership=="Free":
     horses = Horse.objects.all().filter(user=user)[:1]
    elif  user.profile.membership=="Competition":
         horses = Horse.objects.all().filter(user=user)[:5]
    else:
         horses = Horse.objects.all().filter(user=user)
    return render(request, 'horse_details.html', {'horses': horses})

#displays horse details
def detailsInd(request, pk):
    today = datetime.now().date()
   
    user = request.user
    
    selected = Horse.objects.get(pk=pk)


    horses = Horse.objects.all().filter(user=user)
    training = TrainingLog.objects.all().filter(horse=pk).order_by('-date')[:5]
    links = Link.objects.all().filter(horse=pk)
    photos = Images_new.objects.all().filter(horse=pk)
    passport= Images_P.objects.all().filter(horse=pk)

    appointments = Appointment.objects.all().filter(
        horse=selected).order_by('event__appType', 'due')
  


        
      

    return render(request, 'horse_details_ind.html', {'training': training, 'appointments': appointments, 'selected': selected, 'horses': horses, 'links': links,'photos':photos,'passport':passport })


#deletes or edits horse already in db

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

#deletes a horse from db
def deletehorse(request, pk):
    instance = get_object_or_404(Horse, pk=pk)
    instance.delete()
    messages.error(request, "Horse Deleted")

    return redirect(reverse('home'))

#adds image of passport
def savepassport(request,pk):
    selected = Horse.objects.get(pk=pk)
    #random number for id
    rand=random.randint(1,10000)
   
    if request.method == "POST":
            photo = request.FILES.get('id_image_passport')
           
            selected.photo = photo
            selected.save()
            obj=Images_P.objects.create(photo=photo,horse=selected,id=rand)
         
            messages.error(request, "passport Saved")  

         
    
          
            
      
            return JsonResponse({'data':'Data uploaded'})
          
           
          



     
    return redirect(reverse('detailsInd', kwargs={'pk': pk}))