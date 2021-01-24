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
