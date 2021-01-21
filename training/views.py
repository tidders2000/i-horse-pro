from django.shortcuts import render, get_object_or_404, redirect
from horse.models import Horse
from .models import *
from .forms import training_form, objective_form


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

    return render(request, 'tedit.html', {'listObj': listObj, 'obj': obj, 'form': form, 'session': session, })
