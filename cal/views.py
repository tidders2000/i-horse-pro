from django.shortcuts import render
from appointment.models import Appointment
# Create your views here.


def cal(request):
    user = request.user
    events = Appointment.objects.all().filter(user=user)

    return render(request, 'calendar.html', {'events': events})


def calTwo(request):
    user = request.user
    events = Appointment.objects.all().filter(user=user)

    return render(request, 'caltwo.html', {'events': events})
