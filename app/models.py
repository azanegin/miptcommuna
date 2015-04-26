"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    shopName = models.TextField() # название магазина


class ShopTag(models.Model):
    shop = models.ForeignKey(Shop) 
    tag =  models.TextField() # тег к конкретному магазину


class Discount(models.Model):
    owner = models.ForeignKey(User) # владелец скидки
    #shop = models.TextField()
    shop = models.ForeighKey(Shop) # магазин для скидки
    discountType = models.TextField() # тип скидки
    discount = models.FloatField() # размер скидки
    expTime = models.DateField() # время истеченея срока
    description = models.TextField() # описание скидки


class Meeting(models.Model):
    metType = models.TextField() # тип встречи
    time = models.TimeField() # день
    dayPart = models.TextField() # время дня
    location = models.TextField() # место для мероприятия
    creator = models.ForeignKey(User) # создатель
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
    owner = models.ForeignKey(User) # владелец
    quality = models.TextField() # качетво предмета
    location = models.TextField() # где его можно найти
    status = models.BooleanField(default=False) # используется ли сейчас
    isCommon = models.BooleanField(default=True) # общественный
    description = models.TextField() # описание
    

class People(models.Model):
    firstName = models.TextField() # имя
    surname = models.TextField() # фамилия
    secondName = models.TextField() # отчество
    birthday = models.DateField() # день рождения
    department = models.TextField() # факультет
    group = models.TextField() # группа
    vkLink = models.TextField() # ссылка на вк
    fblink = models.TextField() # ссылка на фб
    skype = models.TextField() # ник в скайпе
    physMail = models.TextField() # физтех почта
    mainMail = models.TextField() # оснеовная почта
    phone = models.TextField() #  телефон
    dormNumber = models.DecimalField(max_digits=5, decimal_places=2) # номер общаги
    roomNumber = models.DecimalField(max_digits=5, decimal_places=2) # номер комнаты
    


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
