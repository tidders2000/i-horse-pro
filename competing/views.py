from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponseRedirect
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
from django.contrib import messages
# Create your views here.


def competition(request):
    user = request.user
    customImg = CustomImages.objects.all().filter(user=user)
    request.session['dis'] = 'none'  # sets appointment display css
    return render(request, 'comp.html', {'customImg': customImg})


def comp_create(request, pk):
    customImg = get_object_or_404(CustomImages, pk=pk)
    form = comp_form()
    venue = venue_form()
    user = request.user
    sessionSave = form.save(commit=False)
    sessionSave.disipline = customImg
    sessionSave.user = user

    sessionSave.save()
    print(sessionSave)
    venueSave = venue.save(commit=False)
    venueSave.competition = sessionSave
    venueSave.venueName = 'Venue Name'
    venueSave.save()

    pk = sessionSave.pk

    url = 'comp_edit/{}'.format(pk)
    return redirect(url)


def comp_edit(request, pk):
    session = get_object_or_404(CompetitionLog, pk=pk)
    user = request.user

    test = venue_form()
    form = comp_form(instance=session)
    venue_instance = get_object_or_404(Venue, competition=session)
    print(venue_instance)
    venue = venue_form(venue_instance.pk)
    display = request.session['dis']
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

                messages.error(request, "Entry Added")

                return redirect(reverse('comp_edit', kwargs={'pk': session.pk}) + '#entries')

        if 'save_log' in request.POST:

            log = comp_form(
                request.POST, request.FILES, instance=session)
            if log.is_valid():
                log.save()
                request.session['dis'] = "inline"
                messages.error(request, "Competition Saved")

                url = '/competing/comp_edit/{}'.format(session.pk)
                return redirect(url)
        if 'save_venue' in request.POST:

            venue_update = venue_form(request.POST, instance=venue_instance)
            if venue_update.is_valid():
                venue_update.save()

                messages.error(request, "Info Saved")
                url = '/competing/comp_edit/{}'.format(session.pk)

                return redirect(url)

    return render(request, 'cedit.html', {'venue_instance': venue_instance, 'display': display, 'entry': entry, 'form': form, 'session': session, 'venue': venue, 'entries': entries})


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
    request.session['dis'] = 'none'  # sets appointment display css
    comps = CompetitionLog.objects.all().filter(user=user).order_by('-date')
    paginator = Paginator(comps, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    training = TrainingLog.objects.all().filter(user=user).order_by('-date')
    paginators = Paginator(training, 10)
    train_obj = paginators.get_page(page_number)
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

    return render(request, 'editentry.html', {'form': form, 'comp': comp})
