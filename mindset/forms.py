
from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class goals_form(forms.ModelForm):

    class Meta:

        model = Goals
        exclude = ['user']
