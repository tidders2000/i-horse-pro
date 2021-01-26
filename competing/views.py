from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from training.models import CustomImages
from .forms import *
from training.models import TrainingLog
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
    # venue = venue_form()
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

    return render(request, 'cedit.html', {'entry': entry, 'form': form, 'session': session, 'venue': venue, 'entries': entries})


def history(request):
    user = request.user
    comps = CompetitionLog.objects.all().filter(user=user)
    training = TrainingLog.objects.all().filter(user=user)

    return render(request, 'history.html', {'comps': comps, 'training': training})


def editentry(request, pk):
    instance = get_object_or_404(Comphorse, pk=pk)
    comp = instance.competition.pk
    form = entry_form(instance=instance)
    if request.method == 'POST':
        entry = entry_form(request.POST, instance=instance)
        entry.save()
        return redirect('comp_edit', pk=comp)

    return render(request, 'editentry.html', {'form': form})
