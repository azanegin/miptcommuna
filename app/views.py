"""
Definition of views.
"""
from app.models import Meeting, Person, Item
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.core.files.storage import default_storage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from app.forms import *


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


# http://yuji.wordpress.com/2013/01/30/django-form-field-in-initial-data-requires-a-fieldfile-instance/
class FakeField(object):
    storage = default_storage


fieldfile = FieldFile(None, FakeField, 'dummy.txt')


class HomePageView(TemplateView):
    template_name = 'demo/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'This is a demo of a message.')
        return context


class DefaultFormsetView(FormView):
    template_name = 'demo/formset.html'
    form_class = ContactFormSet


class MeetingFormView(FormView):
    template_name = 'demo/form.html'
    form_class = MeetingForm


class QueryFormView(FormView):
    template_name = 'demo/form.html'
    form_class = QueryForm


class DefaultFormView(FormView):
    template_name = 'demo/form.html'
    form_class = ContactForm


class DefaultFormByFieldView(FormView):
    template_name = 'demo/form_by_field.html'
    form_class = ContactForm


class FormHorizontalView(FormView):
    template_name = 'demo/form_horizontal.html'
    form_class = ContactForm


class FormInlineView(FormView):
    template_name = 'demo/form_inline.html'
    form_class = ContactForm


class FormWithFilesView(FormView):
    template_name = 'demo/form_with_files.html'
    form_class = FilesForm

    def get_context_data(self, **kwargs):
        context = super(FormWithFilesView, self).get_context_data(**kwargs)
        context['layout'] = self.request.GET.get('layout', 'vertical')
        return context

    def get_initial(self):
        return {
            'file4': fieldfile,
        }


class PaginationView(TemplateView):
    template_name = 'demo/pagination.html'

    def get_context_data(self, **kwargs):
        context = super(PaginationView, self).get_context_data(**kwargs)
        lines = []
        for i in range(10000):
            lines.append('Line %s' % (i + 1))
        paginator = Paginator(lines, 10)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results
            show_lines = paginator.page(paginator.num_pages)
        context['lines'] = show_lines
        return context


class MiscView(TemplateView):
    template_name = 'demo/misc.html'


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render_to_response('login.html',
                              context_instance=RequestContext(request))
