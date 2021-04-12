from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import *
from .models import *
from django.contrib import messages


# Create your views here.

def delete_goal(request, pk):
    goal = get_object_or_404(Goals, pk=pk)
    goal.delete()
    messages.error(request, "Goal Deleted")
    return redirect(reverse('home'))


def title_add(request):
    form = titleadd_form()
    user = request.user
    if request.method == 'POST':
        form = titleadd_form(request.POST)
        newObj = form.save(commit=False)
        newObj.user = user
        newObj.save()
        pk = newObj.pk
        return redirect(reverse('mindset', kwargs={'pk': pk}))

    return render(request, 'title_add.html', {'form': form})


def mindset_select(request):
    user = request.user
    instances = Goals.objects.all().filter(user=user)

    return render(request, 'mindset_select.html', {'instances': instances})


def mindset(request, pk):

    user = request.user

    instance = get_object_or_404(Goals, pk=pk)
    if instance:
        form = goals_form(instance=instance)
        if request.method == 'POST':
            goal = goals_form(request.POST, instance=instance)
            goal.save()
            form = goals_form(instance=instance)
            return redirect(reverse('mindset', kwargs={'pk': pk}))

    # else:
    #     form = goals_form()
    #     if request.method == 'POST':
    #         goal = goals_form(request.POST)
    #         if goal.is_valid():
    #             newObj = goal.save(commit=False)
    #             newObj.user = user

    #             newObj.save()

    return render(request, 'mindset.html', {'form': form, 'instance': instance, 'pk': pk})


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


def control(request):
    form=control_diagram_form()
    user=request.user
    controls=ControlDiagram.objects.filter(user=user)

    if request.method == 'POST':
            control = control_diagram_form(request.POST)
            if control.is_valid():
                formSave = control.save(commit=False)
                formSave.user = user
                formSave.save()
                return redirect('control')
               

            
    return render(request, 'mindsetB.html', {'form': form,'controls':controls})