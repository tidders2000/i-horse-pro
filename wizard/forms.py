
from .models import Order
from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _
from training.models import *


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


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]

    credit_card_number = forms.CharField(
        label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(
        label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(
        label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2',
            'county'
        )
