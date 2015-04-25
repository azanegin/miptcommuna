"""
Definition of views.
"""
from app.models import Meeting
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime


def home(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/index.html')


def trips(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/trips.html')


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
