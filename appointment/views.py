from django.shortcuts import render, HttpResponse, get_object_or_404
from django_ical.views import ICalFeed
from .models import *
from .forms import *
from datetime import datetime
from datetime import date
import calendar
import vobject
from django.contrib import messages
# Create your views here.


def appointment(request, pk):
    form = event_form()
    user = request.user
    horse = get_object_or_404(Horse,pk=pk)
   

    display = "none"
    if request.method == "POST":
        form = event_form(request.POST, request.FILES)
        if form.is_valid():
            formSave = form.save(commit=False)
            formSave.user = user
            formSave.horse = horse
            formSave.save()
            display = "inline"
            messages.error(request, "Appointment Saved")
            return redirect ('details')
        else:
            print('error')

    return render(request, 'appointment.html', {'horse':horse,'form': form, 'display': display})


def editapp(request):

    app = request.GET['app']
    instance = get_object_or_404(Appointment, pk=app)
    form = event_form(instance=instance)
    user = request.user
    id = request.GET['horse']
    horse = Horse.objects.get(pk=id)
    display = "none"
    if request.method == "POST":
        form = event_form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            formSave = form.save(commit=False)
            formSave.user = user
            formSave.horse = horse
            formSave.save()
            display = "inline"
            messages.error(request, "Appointment Saved")
        else:
            print('error')

    return render(request, 'appointment.html', {'form': form, 'display': display, 'instance': instance,'horse':horse})


class EventFeed(ICalFeed):
    """
    A simple event calender
    """
    product_id = '-//example.com//Example//EN'
    timezone = 'UTC'
    file_name = "event.ics"

    def __call__(self, request, *args, **kwargs):
        self.user = request.user
        return super(EventFeed, self).__call__(request, *args, **kwargs)

    def items(self):
        return Appointment.objects.filter(user=self.user).order_by('-due')

    def item_guid(self, item):
        return "{}{}".format(item.id, "global_name")

    def item_title(self, item):

        return "{}".format(item.event)

    def item_description(self, item):
        return item.notes

    def item_start_datetime(self, item):
        return item.due

    def item_link(self, item):
        return "http://www.google.de"


# def ical(request, user_id=None):
#     cal = vobject.iCalendar()

#     cal.add('method').value = 'PUBLISH'
#     cal.add('calscale').value = 'GREGORIAN'
#     cal.add('x-wr-calname').value = 'TestCal28'
#     cal.add('x-wr-timezone').value = 'Australia/Sydney'
#     cal.add('x-wr-caldesc').value = ''
#     vevent = cal.add('vevent')
#     vevent.add('dtstart').value = datetime(2021, 1, 22)
#     vevent.add('dtend').value = datetime(2021, 1, 22)
#     vevent.add('dtstamp').value = datetime.now()
#     vevent.add('summary').value = "Test event"
#     icalstream = cal.serialize()

#     response = HttpResponse(icalstream, content_type='text/calendar')
#     response['Filename'] = 'filename.ics'
#     response['Content-Disposition'] = 'attachment; filename=filename.ics'
#     return response
