
from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML


class DateInput(forms.DateInput):
    input_type = 'date'


class horse_form(forms.ModelForm):

    class Meta:
        gender = [('Gelding', 'Gelding'), ('Mare', 'Mare'),
                  ('Stallion', 'Stallion')]
        model = Horse
        fields = ('__all__')

        widgets = {
            'Dob': DateInput()
        }
