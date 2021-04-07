from django.db import models


from django.contrib.auth.models import User
gender = [('Gelding', 'Gelding'), ('Mare', 'Mare'), ('Stallion', 'Stallion')]
tackType = [('Saddle', 'Saddle'), ('Bit', 'Bit'),
            ('Bridle', 'Bridle'), ('Other', 'Other')]


class Horse(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    showName = models.CharField(max_length=100, default='Show Name')
    stableName = models.CharField(max_length=100, default='Stable Name')
    photo = models.ImageField(
        upload_to='media/images/horses', blank=True, default='media/images/horses/horse.jpeg')
    passport = models.ImageField(
        upload_to='media/images/passport', blank=True, default='media/images/passport.jpg')
    breed = models.CharField(max_length=100, default='Irish Cob')
    Gender = models.CharField(max_length=40, choices=gender, default='Gelding')
    pedigree = models.CharField(max_length=200, default='Sire x Dam')
    height = models.DecimalField(max_digits=3, decimal_places=1, default=15.3)
    colour = models.TextField(default="patchy twat")
    Dob = models.DateField(default="2015-01-01")
    owner = models.CharField(max_length=100, default="John Doe")
    owner_mobile =  models.CharField(max_length=20, blank=True)
    owner_email = models.EmailField(max_length=200, blank=True)
    street_address1 = models.CharField(max_length=40, blank=True)
    street_address2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
 
    feeds = models.TextField(blank=True)

    notes = models.TextField(blank=True, default="behaviour etc")

    def __str__(self):
        return self.stableName


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
