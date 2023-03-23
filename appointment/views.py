from django.shortcuts import render, HttpResponse, get_object_or_404,redirect,reverse
from django_ical.views import ICalFeed
from .models import *
from .forms import *
from datetime import datetime
from datetime import date
import calendar
import vobject
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

def get_csrftoken_from_cookie(request, **kwargs):
    return JsonResponse({"token": request.COOKIES["csrftoken"]})

#removes appointment
def deleteAppointment(request, pk):
       instance = get_object_or_404(Appointment, pk=pk)
       instance.delete()


       return redirect("home")
#adds appointment
def appointment(request, pk):
    form = event_form()
    user = request.user
    horse = get_object_or_404(Horse,pk=pk)
   


    if request.method == "POST":
        form = event_form(request.POST, request.FILES)
        if form.is_valid():
            formSave = form.save(commit=False)
            formSave.user = user
            formSave.horse = horse
            formSave.save()
         
            messages.error(request, "Appointment Saved")
            #sends back to horse that appointment made for
            return redirect(reverse('detailsInd', kwargs={'pk': horse.pk}))
         
        else:
            print('error')

    return render(request, 'appointment.html', {'horse':horse,'form': form})

#allows user to edit appointment
def editapp(request):

    app = request.GET['app']
    instance = get_object_or_404(Appointment, pk=app)

    form = event_form(instance=instance)
    user = request.user
    id = request.GET['horse']
    horse = Horse.objects.get(pk=id)
   
    if request.method == "POST":
        photo = request.FILES.get('id_image')
        form = event_form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            formSave = form.save(commit=False)
            formSave.user = user
            formSave.report = photo
            formSave.horse = horse
            formSave.save()
          
            messages.error(request, "Appointment Saved")
            return redirect(reverse('detailsInd', kwargs={'pk': horse.pk}))
        else:
            print('error')

    return render(request, 'appointment.html', {'form': form, 'instance': instance,'horse':horse})

#create ICS file
class EventFeed(ICalFeed):
    """
    A simple event calender
    """
    product_id = '-//example.com//Example//EN'
    timezone = 'UTC'
    file_name = "event.ics"

    def __call__(self, request, *args, **kwargs):
        self.user = request.user
        self.pk = kwargs['pk']
        return super(EventFeed, self).__call__(request, *args, **kwargs)

    def items(self):
        return Appointment.objects.filter(pk=self.pk)

    def item_guid(self, item):
        return "{}{}".format(item.id, "global_name")

    def item_title(self, item):

        return "{}".format(item.event)

    def item_description(self, item):
        return item.notes

    def item_start_datetime(self, item):
        return item.due

    def item_link(self, item):
        return "http://i-horse.co.uk"


