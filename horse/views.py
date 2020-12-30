from django.shortcuts import render
from .forms import horse_form

# Create your views here.


def horse(request):
    form = horse_form()
    return render(request, 'horse.html', {'form': form})
