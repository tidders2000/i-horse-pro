from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.contrib import messages

# Create your views here.


def people(request):
    user = request.user
 
    if user.profile.membership!="Pro":
         messages.error(request, 'Sorry you need Pro Membership to access Yard Management') 
         return redirect('home')
    user = request.user
    client = Client.objects.filter(user=user)

    employee = Staff.objects.filter(user=user)
    return render(request, 'people.html', {'client': client, 'employee': employee})


def clients(request):
    user = request.user
    form = client_form()
    if request.method == "POST":
       
        form_add = client_form(request.POST, request.FILES)
    
        if form_add.is_valid():
            formSave = form_add.save(commit=False)
            formSave.user = request.user
        
            formSave.save()
            messages.error(request, "Client Saved")
    return render(request, 'client.html', {'form': form})


def staff(request):
    user = request.user
 
    if user.profile.membership!="Pro":
         messages.error(request, 'Sorry you need Pro Membership to access Yard Management') 
         return redirect('home')
    form = staff_form()
    if request.method == "POST":
        form_add = staff_form(request.POST)
        if form_add.is_valid():
            formSave = form_add.save(commit=False)
            formSave.user = request.user
            formSave.save()
            messages.error(request, "Employee Saved")
    return render(request, 'staff.html', {'form': form})


def yard_menu(request):
    user = request.user
 
    if user.profile.membership!="Pro":
         messages.error(request, 'Sorry you need Pro Membership to access Yard Management') 
         return redirect('home')
 
    if request.method == "POST":
      fname=request.POST.get('fn')
      lname= request.POST.get('ln')
      print(fname)
      print(lname)

    return render(request, 'yard_menu.html')


def edit_client(request, pk):
    instance = get_object_or_404(Client, pk=pk)
    form = client_form(instance=instance)

    if request.method == "POST":
        form_add = client_form(request.POST,request.FILES, instance=instance)
        if form_add.is_valid():
            form_add.save()
            messages.error(request, "Client Updated")
            return redirect('people')
    return render(request, 'client.html', {'form': form, 'instance': instance})


def edit_staff(request, pk):
    instance = get_object_or_404(Staff, pk=pk)
    form = staff_form(instance=instance)
    if request.method == "POST":
        form_add = staff_form(request.POST, instance=instance)
        if form_add.is_valid():
            form_add.save()
            messages.error(request, "Employee Updated")
            return redirect('people')

    return render(request, 'staff.html', {'form': form, 'instance': instance})


def delete_staff(request, pk):
    instance = get_object_or_404(Staff, pk=pk)
    instance.delete()
    return redirect('people')


def delete_client(request, pk):
    instance = get_object_or_404(Client, pk=pk)
    instance.delete()
    return redirect('people')
