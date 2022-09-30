
from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML
from datetimepicker.widgets import DateTimePicker
from django.forms import DateTimeField

# class DateInput(forms.DateInput):
#     input_type = 'date'


# class TimeInput(forms.TimeInput):
#     input_type = "time"


class event_form(forms.ModelForm):
    due= DateTimeField(input_formats='%m/%d/%Y %H:%M')
    class Meta:

        model = Appointment
        exclude = ['user', 'horse','link','report']
  
     