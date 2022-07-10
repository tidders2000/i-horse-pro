from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class client_form(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'start_date': DateInput(),
        }


class staff_form(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        exclude = ['user']
     
