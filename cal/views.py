from django.shortcuts import render
from appointment.models import Appointment
from training.models import TrainingLog
from competing.models import CompetitionLog
# Create your views here.





def calTwo(request):
    user = request.user
    events = Appointment.objects.all().filter(user=user)
    training = TrainingLog.objects.all().filter(user=user)
    competition = CompetitionLog.objects.all().filter(user=user)

    return render(request, 'caltwo.html', {'events': events, 'training': training, 'competition': competition})
