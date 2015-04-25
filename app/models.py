"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class Discount(models.Model):
    owner = models.ForeignKey(User)
    shop = models.TextField()
    discountType = models.TextField()
    discount = models.FloatField()
    expTime = models.DateField()
    description = models.TextField()

class Meeting(models.Model):
    metType = models.TextField()
    time = models.TimeField()
    location = models.TextField()
    creator = models.ForeignKey(User)
    support = models.TextField()
    money = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

class Member(models.Model):
    meeting = models.ForeignKey(Meeting)
    user = models.ForeignKey(User)
    donate = models.DecimalField(max_digits=5, decimal_places=2)

class Item(models.Model):
    name = models.TextField()
    owner = models.ForeignKey(User)
    quality = models.TextField()
    location = models.TextField()
    isCommon = models.BooleanField(default=True)

class People(models.Model):
    roomNumber = models.DecimalField(max_digits=5, decimal_places=2)
    dormNumber = models.DecimalField(max_digits=5, decimal_places=2)
