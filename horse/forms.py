
from django import forms
from django.forms import Textarea
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML


class DateInput(forms.DateInput):
    input_type = 'date'


class wizard_horse_form(forms.ModelForm):
    class Meta:
        model = Horse
        fields = ['stableName', 'photo']
        widgets = {
            'notes':Textarea(attrs={'cols':20,'rows':20})
        }


class horse_wizard(forms.ModelForm):

    class Meta:

        model = Horse
        fields = ['stableName']
        widgets = {
            'notes':Textarea(attrs={'cols':20,'rows':20})
        }


class horse_form(forms.ModelForm):

    class Meta:
        gender = [('Gelding', 'Gelding'), ('Mare', 'Mare'),
                  ('Stallion', 'Stallion')]
        model = Horse
        exclude = ['user']
        widgets = {
            'notes':Textarea(attrs={'cols':20,'rows':20})
        }


class link_form(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('organisation', 'link')


class tack_form(forms.ModelForm):
    class Meta:
        model = Tack
        fields = ('tacktype', 'description')
