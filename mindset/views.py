from django.shortcuts import render, redirect
from .forms import *


# Create your views here.


def mindset(request):

    user = request.user

    instance = Goals.objects.all().filter(user=user).first()
    if instance:
        form = goals_form(instance=instance)
        if request.method == 'POST':
            goal = goals_form(request.POST, instance=instance)
            goal.save()
            form = goals_form(instance=instance)
        return render(request, 'mindset.html', {'form': form, 'instance': instance})

    else:
        form = goals_form()
        if request.method == 'POST':
            goal = goals_form(request.POST)
            if goal.is_valid():
                newObj = goal.save(commit=False)
                newObj.user = user

                newObj.save()

    return render(request, 'mindset.html', {'form': form, 'instance': instance})


def mindsetB(request):
    user = request.user

    instance = Control.objects.all().filter(user=user).first()
    if instance:
        form = control_form(instance=instance)
        if request.method == 'POST':
            control = control_form(request.POST, instance=instance)
            control.save()
            form = control_form(instance=instance)
        return render(request, 'mindsetB.html', {'form': form, 'instance': instance})

    else:
        form = control_form()
        if request.method == 'POST':
            control = control_form(request.POST)
            if control.is_valid():
                newObj = control.save(commit=False)
                newObj.user = user

                newObj.save()

    return render(request, 'mindsetB.html', {'form': form, 'instance': instance})
