from django.contrib import admin
from app.models import Discount, Meeting, Member, Item, Person
from django.contrib.auth.models import User

admin.site.register(Discount)
admin.site.register(Member)
admin.site.register(Meeting)
admin.site.register(Item)
admin.site.register(Person)
