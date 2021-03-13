from django.db import models
from phone_field import PhoneField
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User
# Create your models here.


class Staff(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True)

    street_address1 = models.CharField(max_length=40, blank=True)
    street_address2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    mobile = PhoneField(blank=True, help_text='Contact phone number')
    emergency_contact_name = models.CharField(max_length=40, blank=True)
    emergency_contact_number = PhoneField(
        blank=True, help_text='Contact phone number')
    start_date = models.DateField()
    termination_date = models.DateField()
    pay_rate = MoneyField(max_digits=14, decimal_places=2,
                          default_currency='GBP')
    notes = models.TextField()

    def __str__(self):
        return self.name


class Client  (models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True)
    start_date = models.DateField()
    street_address1 = models.CharField(max_length=40, blank=True)
    street_address2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    mobile = PhoneField(blank=True, help_text='Contact phone number')
    emergency_contact_name = models.CharField(max_length=40, blank=True)
    emergency_contact_number = PhoneField(
        blank=True, help_text='Contact phone number')

    def __str__(self):
        return self.name
