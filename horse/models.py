from django.db import models


from django.contrib.auth.models import User
gender = [('Gelding', 'Gelding'), ('Mare', 'Mare'), ('Stallion', 'Stallion')]


class Horse(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    showName = models.CharField(max_length=100, default='Show Name')
    stableName = models.CharField(max_length=100, default='Stable Name')
    photo = models.ImageField(
        upload_to='media/images/horses', blank=True, default='')
    breed = models.CharField(max_length=100, default='Irish Cob')
    Gender = models.CharField(max_length=40, choices=gender, default='Gelding')
    pedigree = models.CharField(max_length=200, default='Sire x Dam')
    height = models.DecimalField(max_digits=3, decimal_places=1, default=15.3)
    markings = models.TextField(default="patchy twat")
    Dob = models.DateField(auto_now_add=True)
    owner = models.CharField(max_length=100, default="John Doe")
    street_address1 = models.CharField(max_length=40, blank=True)
    street_address2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    usefulllinks = models.TextField()

    def __str__(self):
        return self.user
