from django.shortcuts import render, redirect, get_object_or_404
from training.models import CustomImages
from .forms import *
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

        if 'save_log' in request.POST:
            log = comp_form(
                request.POST, request.FILES, instance=session)
            if log.is_valid():
                log.save()

        if 'save_venue' in request.POST:
            ven = venue_form(request.POST)
            if ven.is_valid():
                newObj = ven.save(commit=False)
                newObj.venueName = session.location
                newObj.competition = session

                newObj.save()

    return render(request, 'cedit.html', {'entry': entry, 'form': form, 'session': session, 'venue': venue, 'entries': entries})
