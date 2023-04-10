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
from django.core.paginator import Paginator

# ics file creation du0plkicated due to different setting for comp

class EventFeed3(ICalFeed):
    """
    A simple event calender
    """
    product_id = '-//example.com//Example//EN'
    timezone = 'UTC'
    file_name = "comp.ics"

    def __call__(self, request, *args, **kwargs):
        self.user = request.user
        self.pk = kwargs['pk']
        return super(EventFeed3, self).__call__(request, *args, **kwargs)
        print(self.user)

    def items(self):
        return TrainingLog.objects.filter(pk=self.pk)

    def item_guid(self, item):
        return "{}{}".format(item.id, "global_name")

    def item_title(self, item):

        return "Training:{}".format(item.horse)

    def item_description(self, item):
        return item.disipline

    def item_start_datetime(self, item):
        return item.date

    def item_link(self, item):
        return "http://www.google.de"

#create training log
def training_log(request):
    user = request.user
    #gets the dispine image as set by admin
    customImg = Disipline.objects.all()
     #create serch and history
    train = TrainingLog.objects.all().filter(user=user).order_by('-date')
    paginator = Paginator(train, 10)
    page_number = request.GET.get('page')
    train_obj = paginator.get_page(page_number)
    page_obj = paginator.get_page(page_number)

    return render(request, 'tlog.html', {'customImg': customImg,'train_obj': train_obj,'page_obj':page_obj})

#creates  TRAINING EVENT    
def training_create(request, pk):

    customImg = get_object_or_404(Disipline, pk=pk)
    form = training_form(request.user)
    user = request.user
    sessionSave = form.save(commit=False)
    sessionSave.disipline = customImg
    sessionSave.user = user
    sessionSave.save()
    pk = sessionSave.pk
    url = 'training_edit/{}'.format(pk)
    return redirect(url)
#edit a training event

def training_edit(request, pk):
    session = get_object_or_404(TrainingLog, pk=pk)
    user = request.user
    form = training_form(request.user,instance=session)
    listObj = Objectives.objects.all().filter(session=session)
    obj = objective_form()
# saves objectives
    if request.method == 'POST':
        
        if 'save_obj' in request.POST:
            obj = objective_form(request.POST)
            if obj.is_valid():

                newObj = obj.save(commit=False)
                newObj.user = user
                newObj.session = session
                newObj.save()
                return redirect(reverse('training_edit', kwargs={'pk': pk}) + '#obj')
#saves edit to training
        if 'save_log' or 'floor_plan' in request.POST:
            photo = request.FILES.get('id_image')
            log = training_form(request.user,
                request.POST, request.FILES, instance=session)
            if log.is_valid():
                 formSave = log.save(commit=False)
                 formSave.files = photo
                 formSave.save()
               
                # display = 'inline'
                 messages.error(request, "Training Saved")

                 if 'floor_plan' in request.POST:
                       return redirect("draw", pk=pk)
                 return redirect("training_edit", pk=pk)
                

    return render(request, 'tedit.html', {'pk': pk, 'listObj': listObj, 'obj': obj, 'form': form, 'session': session})

#code to toggle objective done icon off and on
def checkOb(request, pk):
    objective = get_object_or_404(Objectives, pk=pk)
    if objective.Completed == False:
        objective.Completed = True
    else:
        objective.Completed = False

    objective.save()
    session = objective.session.pk
    return redirect("training_edit", pk=session)

# deletes an objective
def deleteobjective(request,pk):
    objective = get_object_or_404(Objectives, pk=pk)
    objective.delete()
    id=objective.session.pk
  

    return redirect(reverse('training_edit', kwargs={'pk': id}))

# draw js plugin on the template that allows user to draw a diagram
def draw(request, pk):

    pk = pk

    return render(request, 'draw.html', {'pk': pk})
# saves drawing

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
