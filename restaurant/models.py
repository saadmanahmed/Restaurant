from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Restaurant(models.Model):
    name=models.TextField(blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    cityname=models.TextField(blank=True,null=True)
    type=models.TextField(blank=True,null=True)
    maxaccommodation=models.TextField(blank=True,null=True)
    telephoneumber=models.IntegerField()
    user = models.ForeignKey(User, related_name="restaurant", on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    def __str__(self):
        return str(self.name)

class Dishes(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="myrestaurants", blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, null=True, related_name='dishes',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)

