from django.db import models
from django.forms import ModelForm, Textarea

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    website = models.CharField(max_length=50)

class Address(models.Model):
    street = models.CharField(max_length=50)
    suite = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    users = models.ForeignKey(Users, related_name="address", on_delete=models.CASCADE)

class Geo(models.Model):
    lat = models.CharField(max_length=10)
    lng = models.CharField(max_length=10)
    address = models.ForeignKey(Address, related_name="geo", on_delete=models.CASCADE)

class Company(models.Model):
    name = models.CharField(max_length=50)
    catchPhrase = models.CharField(max_length=50)
    bs = models.CharField(max_length=50)
    users = models.ForeignKey(Users, related_name="company", on_delete=models.CASCADE)
