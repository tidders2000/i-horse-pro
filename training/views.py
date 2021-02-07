from django.shortcuts import render, reverse, get_object_or_404, redirect
from horse.models import Horse
from .models import *
from django_ical.views import ICalFeed
from .forms import training_form, objective_form
from datetime import datetime
from datetime import date
import calendar
from django.contrib import messages
import uuid
import base64
from django.core.files.base import ContentFile


class EventFeed3(ICalFeed):
    """
    A simple event calender
    """
    product_id = '-//example.com//Example//EN'
    timezone = 'UTC'
    file_name = "comp.ics"

    def __call__(self, request, *args, **kwargs):
        self.user = request.user
        return super(EventFeed3, self).__call__(request, *args, **kwargs)
        print(self.user)

    def items(self):
        return TrainingLog.objects.filter(user=self.user).order_by('-date')

    def item_guid(self, item):
        return "{}{}".format(item.id, "global_name")

    def item_title(self, item):

        return "{}".format(item.location)

    def item_description(self, item):
        return item.notes

    def item_start_datetime(self, item):
        return item.date

    def item_link(self, item):
        return "http://www.google.de"


def training_log(request):
    user = request.user
    customImg = CustomImages.objects.all().filter(user=user)

    return render(request, 'tlog.html', {'customImg': customImg})


def training_create(request, pk):

    customImg = get_object_or_404(CustomImages, pk=pk)
    form = training_form()
    user = request.user
    sessionSave = form.save(commit=False)
    sessionSave.disipline = customImg
    sessionSave.user = user
    sessionSave.save()
    pk = sessionSave.pk
    url = 'training_edit/{}'.format(pk)
    return redirect(url)


def training_edit(request, pk):
    session = get_object_or_404(TrainingLog, pk=pk)
    user = request.user
    form = training_form(instance=session)
    listObj = Objectives.objects.all().filter(session=session)
    obj = objective_form()
    if request.method == 'POST':

        if 'save_obj' in request.POST:
            obj = objective_form(request.POST)
            if obj.is_valid():

                newObj = obj.save(commit=False)
                newObj.user = user
                newObj.session = session
                newObj.save()

        if 'save_log' in request.POST:
            log = training_form(
                request.POST, request.FILES, instance=session)
            if log.is_valid():
                log.save()
                messages.error(request, "Training Saved")

    return render(request, 'tedit.html', {'listObj': listObj, 'obj': obj, 'form': form, 'session': session, })


def checkOb(request, pk):
    objective = get_object_or_404(Objectives, pk=pk)
    if objective.Completed == False:
        objective.Completed = True
    else:
        objective.Completed = False

    objective.save()
    session = objective.session.pk
    return redirect("training_edit", pk=session)


def draw(request, pk):

    pk = pk

    return render(request, 'draw.html', {'pk': pk})


def savedraw(request, pk):
    session = get_object_or_404(TrainingLog, pk=pk)

    if request.method == "POST":
        canvas = request.POST.get('imagedata')
        format, imgstr = canvas.split(';base64,')
        print("format", format)
        ext = format.split('/')[-1]
        string = uuid.uuid4().hex[:6].upper()
        print(string)
        data = ContentFile(base64.b64decode(imgstr))
        file_name = "mydraw{}.".format(string) + ext
        print(file_name)
        session.floorPlan.save(file_name, data, save=True)

    return redirect(reverse('training_edit', kwargs={'pk': session.pk}))
