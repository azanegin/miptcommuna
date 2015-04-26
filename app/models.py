"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User)
    roomNumber = models.DecimalField(max_digits=5, decimal_places=0)
    dormNumber = models.DecimalField(max_digits=5, decimal_places=0)


class Discount(models.Model):
    owner = models.ForeignKey(Person)
    shop = models.TextField()
    discountType = models.TextField()
    discount = models.FloatField()
    expTime = models.DateField()
    description = models.TextField()


class Meeting(models.Model):
    metType = models.TextField()
    time = models.TimeField()
    location = models.TextField()
    creator = models.ForeignKey(Person)
    support = models.TextField()
    money = models.DecimalField(max_digits=5, decimal_places=0)
    description = models.TextField()


class Member(models.Model):
    meeting = models.ForeignKey(Meeting)
    user = models.ForeignKey(Person)
    donate = models.DecimalField(max_digits=5, decimal_places=0)


class Item(models.Model):
    name = models.TextField()
    owner = models.ForeignKey(Person)
    quality = models.TextField()
    location = models.TextField()
    isCommon = models.BooleanField(default=True)
