"""
Definition of views.
"""
from app.models import Meeting, Person, Item
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import render, get_object_or_404

def home(request):
    assert isinstance(request, HttpRequest)
    context = {'items': Item.objects.all()}
    return render(request, 'app/index.html', context)


def trips(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/trips.html')

def person(request, person_id):
    assert isinstance(request, HttpRequest)
    context = {'person': get_object_or_404(Person, pk=person_id)}
    return render(request, 'app/person.html', context)


def item(request, item_id):
    assert isinstance(request, HttpRequest)
    context = {'item': get_object_or_404(Item, pk=item_id)}
    return render(request, 'app/item.html', context)


def meetings(request):
    assert isinstance(request, HttpRequest)
    context = Meeting.objects.all()
    return render(request, 'app/meetings.html', context)


def post_wanted(request):
    assert isinstance(request, HttpRequest)
    context = {}
    return render(request, 'app/wantedform.html')


def post(request):
    assert isinstance(request, HttpRequest)
    context = {}
    return render(request, 'app/form')
