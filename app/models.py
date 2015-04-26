"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User)
    department = models.TextField(default='') # факультет
    group = models.TextField(default='') # группа
    vkLink = models.TextField(default='') # ссылка на вк
    fblink = models.TextField(default='') # ссылка на фб
    skype = models.TextField(default='') # ник в скайпе
    physMail = models.TextField(default='') # физтех почта
    mainMail = models.TextField(default='') # оснеовная почта
    phone = models.TextField(default='') #  телефон
    dormNumber = models.DecimalField(max_digits=5, decimal_places=0) # номер общаги
    roomNumber = models.DecimalField(max_digits=5, decimal_places=0) # номер комнаты

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


class Shop(models.Model):
    shopName = models.TextField() # название магазина

class ShopTag(models.Model):
    shop = models.ForeignKey(Shop) 
    tag =  models.TextField() # тег к конкретному магазину

class Discount(models.Model):
    owner = models.ForeignKey(Person) # владелец скидки
    shop = models.ForeignKey(Shop) # магазин для скидки
    discountType = models.TextField() # тип скидки
    discount = models.FloatField() # размер скидки
    expTime = models.DateField() # время истеченея срока
    description = models.TextField() # описание скидки

class Meeting(models.Model):
    metType = models.TextField() # тип встречи
    time = models.TimeField() # день
    dayPart = models.TextField() # время дня
    location = models.TextField(default='') # место для мероприятия
    creator = models.ForeignKey(Person) # создатель
    support = models.TextField() # поддержка от МКИ, Деканата и так далее
    money = models.DecimalField(max_digits=5, decimal_places=2) # стоимость для участия
    description = models.TextField() # описание события
    link = models.TextField() #  ссылка на событие в вк
    

class Member(models.Model):
    meeting = models.ForeignKey(Meeting) # встреча
    user = models.ForeignKey(User) # учаник встречи
    donate = models.DecimalField(max_digits=5, decimal_places=2) # его взнос


class Gallery(models.Model):
    meet = models.ForeignKey(Meeting) # встреча
    uploader = models.ForeignKey(User) # кто дал доступ к галлерее
    link = models.TextField() # ссылка на галлерею


class Item(models.Model):
    name = models.TextField() # название предмета
    itemType = models.TextField() # классификация предмета
    owner = models.ForeignKey(Person) # владелец
    quality = models.TextField() # качетво предмета
    location = models.TextField() # где его можно найти
    status = models.BooleanField(default=False) # используется ли сейчас
    isCommon = models.BooleanField(default=True) # общественный
    description = models.TextField() # описание
    

    


class Query(models.Model):
    who = models.ForeignKey(User) # кто
    need = models.TextField() #  что ищет
    time = models.TimeField() # на какой день
    dayPart = models.TextField() # время суток
    duration = models.TextField() # длительность
    description = models.TextField() # описание
    compelete = models.BooleanField(default=False) # удовлетворен
    cancel = models.BooleanField(default=False) # отменен
    
class Squery(models.Model):
    query = models.ForeignKey(Query) # запрос
    person = models.ForeignKey(User) # пользователь

