from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class comp_form(forms.ModelForm):

    class Meta:

        model = CompetitionLog
        fields = ['myStars', 'notes', 'lightbulb',
                  'image', 'videoLink', 'date', 'location']


class entry_form(forms.ModelForm):
    class Meta:
        model = Comphorse
        exclude = ['user', 'competition']


class venue_form(forms.ModelForm):
    class Meta:
        model = Venue
        exclude = ['venueName', 'competition']
