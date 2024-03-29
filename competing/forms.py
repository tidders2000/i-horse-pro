from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _


class DateInput(forms.DateInput):
    input_type = 'date'


class comp_form(forms.ModelForm):

    class Meta:

        model = CompetitionLog
        exclude = ['videoLink',]
        fields = ['myStars', 'performance', 'lightbulb',
                  'image', 'videoLink', 'date', 'location']
        labels = {
            'location': _('* Location'),
              'date': _('* Date')
        }


class entry_form(forms.ModelForm):
    class Meta:
        model = Comphorse
        exclude = ['user', 'competition']
        widgets = {
            'horse': forms.Select(
                attrs={'class': 'bum'}
            ),
            'class_time': forms.TimeInput(attrs={'type': 'time'})
        }


class venue_form(forms.ModelForm):
    class Meta:
        model = Venue
        exclude = ['venueName', 'competition']
