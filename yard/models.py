from django.db import models
from phone_field import PhoneField
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User
# Create your models here.


class Staff(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True)

    street_address1 = models.CharField(max_length=40, blank=True)
    street_address2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    mobile = models.CharField(max_length=40, blank=True)
    emergency_contact_name = models.CharField(max_length=40, blank=True)
    emergency_contact_number = models.CharField(max_length=40, blank=True)
    start_date = models.DateField(blank=True,null=True)
    ni_number = models.CharField(max_length=20, blank=True)
    
    
   
    pay_rate = models.CharField(max_length=40, blank=True)
    notes = models.TextField(blank=True)
    termination_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Client  (models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True)

    street_address1 = models.CharField(max_length=40, blank=True)
    street_address2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    mobile = models.CharField(max_length=40, blank=True)
    emergency_contact_name = models.CharField(max_length=40, blank=True)
    emergency_contact_number = models.CharField(max_length=40, blank=True)
    start_date = models.DateField(blank=True,null=True)
    notes = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='media/images/clients', blank=True, default='media/images/clients/profile.png')
    def __str__(self):
        return self.name
