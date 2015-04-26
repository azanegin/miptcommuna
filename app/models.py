"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    shopName = models.TextField()


class ShopTag(models.Model):
    shop = models.ForeignKey(Shop)
    tag =  models.TextField()


class Discount(models.Model):
    owner = models.ForeignKey(User)
    #shop = models.TextField()
    shop = models.ForeighKey(Shop)
    discountType = models.TextField()
    discount = models.FloatField()
    expTime = models.DateField()
    description = models.TextField()


class Meeting(models.Model):
    metType = models.TextField()
    time = models.TimeField() # day
    dayPart = models.TextField() # time
    location = models.TextField() 
    creator = models.ForeignKey(User)
    support = models.TextField()
    money = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    link = models.TextField()
    

class Member(models.Model):
    meeting = models.ForeignKey(Meeting)
    user = models.ForeignKey(User)
    donate = models.DecimalField(max_digits=5, decimal_places=2)


class Gallery(models.Model):
    meet = models.ForeignKey(Meeting)
    uploader = models.ForeignKey(User)
    link = models.TextField()


class Item(models.Model):
    name = models.TextField()
    itemType = models.TextField()
    owner = models.ForeignKey(User)
    quality = models.TextField()
    location = models.TextField()
    status = models.BooleanField(default=False)
    isCommon = models.BooleanField(default=True)
    description = models.TextField()
    

class People(models.Model):
    firstName = models.TextField()
    surname = models.TextField()
    secondName = models.TextField()
    department = models.TextField()
    group = models.TextField()
    vkLink = models.TextField()
    fblink = models.TextField()
    skype = models.TextField()
    physMail = models.TextField()
    mainMail = models.TextField()
    phone = models.TextField()
    roomNumber = models.DecimalField(max_digits=5, decimal_places=2)
    dormNumber = models.DecimalField(max_digits=5, decimal_places=2)


class Query(models.Model):
    who = models.ForeignKey(User)
    need = models.TextField()
    time = models.TimeField()
    dayPart = models.TextField()
    duration = models.TextField()
    description = models.TextField()
    compelete = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)
    
class Squery(models.Model):
    query = models.ForeignKey(Query)
    person = models.ForeignKey(User)
