
from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class training_form(forms.ModelForm):

    class Meta:

        model = TrainingLog
        exclude = ['user', 'disipline']


class objective_form(forms.ModelForm):
    class Meta:
        model = Objectives
        exclude = ['user', 'session']
