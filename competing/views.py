from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from training.models import CustomImages
from .forms import *
from django_ical.views import ICalFeed
from django.db.models import Q
from training.models import TrainingLog
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import datetime
from datetime import date
import calendar
# Create your views here.


def competition(request):
    user = request.user
    customImg = CustomImages.objects.all().filter(user=user)

    return render(request, 'comp.html', {'customImg': customImg})


def comp_create(request, pk):
    customImg = get_object_or_404(CustomImages, pk=pk)
    form = comp_form()
    user = request.user
    sessionSave = form.save(commit=False)
    sessionSave.disipline = customImg
    sessionSave.user = user
    sessionSave.save()
    pk = sessionSave.pk

    url = 'comp_edit/{}'.format(pk)
    return redirect(url)


def comp_edit(request, pk):
    session = get_object_or_404(CompetitionLog, pk=pk)
    user = request.user
    form = comp_form(instance=session)
    venue = venue_form()
    display = "display"
    # entries = Comphorse.objects.all().filter(session=session)
    entry = entry_form()
    entries = Comphorse.objects.all().filter(competition=session)
    if request.method == 'POST':

        if 'save_entry' in request.POST:
            ent = entry_form(request.POST)
            if ent.is_valid():

                newObj = ent.save(commit=False)
                newObj.user = user
                newObj.competition = session
                newObj.save()
                url = '/competing/comp_edit/{}'.format(session.pk)

                return redirect(url)

        if 'save_log' in request.POST:
            log = comp_form(
                request.POST, request.FILES, instance=session)
            if log.is_valid():
                log.save()
                display = "inline"
                print(display)
                url = '/competing/comp_edit/{}'.format(session.pk)
                return redirect(url)

        if 'save_venue' in request.POST:
            ven = venue_form(request.POST)
            if ven.is_valid():
                newObj = ven.save(commit=False)
                newObj.venueName = session.location
                newObj.competition = session

                newObj.save()
                url = '/competing/comp_edit/{}'.format(session.pk)
                return redirect(url)

    return render(request, 'cedit.html', {'display': display, 'entry': entry, 'form': form, 'session': session, 'venue': venue, 'entries': entries})


class EventFeed2(ICalFeed):
    """
    A simple event calender
    """
    product_id = '-//example.com//Example//EN'
    timezone = 'UTC'
    file_name = "comp.ics"

    def __call__(self, request, *args, **kwargs):
        self.user = request.user
        return super(EventFeed2, self).__call__(request, *args, **kwargs)
        print(self.user)

    def items(self):
        return CompetitionLog.objects.filter(user=self.user).order_by('-date')

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


def history(request):
    user = request.user
    comps = CompetitionLog.objects.all().filter(user=user).order_by('-date')
    paginator = Paginator(comps, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    training = TrainingLog.objects.all().filter(user=user).order_by('-date')
    paginators = Paginator(training, 10)
    train_obj = paginator.get_page(page_number)
    if request.method == "POST":
        keyword = request.POST.get('keyword')
        comps = CompetitionLog.objects.filter(
            Q(location__icontains=keyword) | Q(date__icontains=keyword) | Q(disipline__disipline__icontains=keyword))
        paginator = Paginator(comps, 10)
        page_obj = paginator.get_page(page_number)
        training = CompetitionLog.objects.filter(
            Q(location__icontains=keyword) | Q(date__icontains=keyword) | Q(disipline__disipline__icontains=keyword))
        paginators = Paginator(training, 10)
        train_obj = paginator.get_page(page_number)
    return render(request, 'history.html', {'train_obj': train_obj, 'page_obj': page_obj})


def editentry(request, pk):
    instance = get_object_or_404(Comphorse, pk=pk)
    comp = instance.competition.pk
    form = entry_form(instance=instance)
    if request.method == 'POST':
        entry = entry_form(request.POST, instance=instance)
        entry.save()
        return redirect('comp_edit', pk=comp)

    return render(request, 'editentry.html', {'form': form})
