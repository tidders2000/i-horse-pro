
from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _


class DateInput(forms.DateInput):
    input_type = 'date'


class wizard_form(forms.ModelForm):
    class Meta:
        model = CustomImages
        exclude = ['user']


class training_form(forms.ModelForm):

    class Meta:

        model = TrainingLog
        exclude = ['user', 'disipline']
        labels = {
            'location': _('* Location'),
            'date': _('*')
        }


class objective_form(forms.ModelForm):
    class Meta:
        model = Objectives
        exclude = ['user', 'session']
