from django.db import models
from .utils import image_resize

from django.contrib.auth.models import User
gender = [('Gelding', 'Gelding'), ('Mare', 'Mare'), ('Stallion', 'Stallion')]
tackType = [('Saddle', 'Saddle'), ('Bit', 'Bit'),
            ('Bridle', 'Bridle'), ('Other', 'Other')]


class Horse(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    showName = models.CharField(max_length=100)
    stableName = models.CharField(max_length=100,)
    photo = models.FileField(
        upload_to='media/images/horses', blank=True, default='media/images/horses/horse.jpeg')
    passport = models.ImageField(
        upload_to='media/images/passport', blank=True, default='media/images/passport.jpg')
    breed = models.CharField(max_length=100,blank=True)
    Gender = models.CharField(max_length=40, choices=gender, default='Gelding')
    pedigree = models.CharField(max_length=200,blank=True)
    height = models.CharField(max_length=4,blank=True)
    colour = models.TextField(blank=True)
    chip = models.CharField(max_length=100, blank=True)
    Dob = models.DateField(blank=True,null=True)
    owner = models.CharField(max_length=100,blank=True)
    owner_mobile =  models.CharField(max_length=20, blank=True)
    owner_email = models.EmailField(max_length=200, blank=True)
    street_address1 = models.CharField(max_length=40, blank=True)
    street_address2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    Arrived = models.DateField(blank=True,null=True)
    Left = models.DateField(blank=True,null=True)
    feeds = models.TextField(blank=True)

    notes = models.TextField(blank=True, default="behaviour etc")

    def __str__(self):
        return f"{self.stableName}"

    def save(self, *args, **kwargs):
        image_resize(self.photo, 500, 500)
        image_resize(self.passport, 500, 500)
        super().save(*args, **kwargs)

   
class Images(models.Model):
    id = models.CharField(max_length=40,primary_key=True)
    horse = models.ForeignKey(Horse, default=None,on_delete=models.CASCADE)
    photo = models.FileField(
        upload_to='media/images/horses', blank=True, default='media/images/horses/horse.jpeg')
    def save(self, *args, **kwargs):
        image_resize(self.photo, 500, 500)
        
        super().save(*args, **kwargs)

   
class Images_new(models.Model):
    horse = models.ForeignKey(Horse, default=None,on_delete=models.CASCADE)
    photo = models.FileField(
        upload_to='media/images/horses', blank=True, default='media/images/horses/horse.jpeg')
    def save(self, *args, **kwargs):
        image_resize(self.photo, 500, 500)
        
        super().save(*args, **kwargs)

class Link(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    horse = models.ForeignKey(Horse, null=True, on_delete=models.CASCADE)
    organisation = models.CharField(max_length=100)
    link = models.CharField(max_length=100)


class Tack(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    horse = models.ForeignKey(Horse, null=True, on_delete=models.CASCADE)
    tacktype = models.CharField(
        max_length=40, choices=tackType, default='Saddle')
    description = models.CharField(max_length=256, default='Description')
