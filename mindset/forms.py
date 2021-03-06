
from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _


class DateInput(forms.DateInput):
    input_type = 'date'


class titleadd_form(forms.ModelForm):
    class Meta:
        model = Goals
        fields = ['title']


class goals_form(forms.ModelForm):

    class Meta:

        model = Goals
        exclude = ['user']


class control_form(forms.ModelForm):

    class Meta:

        model = Control
        exclude = ['user']
        labels = {
            'can_control': _('Can Control- seperate entries with ,'),
            'cannot_control': _('Cannot Control- seperate entries with ,')
        }
