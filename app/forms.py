# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms.formsets import BaseFormSet, formset_factory
from datetimewidget.widgets import DateTimeWidget

from bootstrap3.tests import TestForm

RADIO_CHOICES = (
    ('1', 'Radio 1'),
    ('2', 'Radio 2'),
)

MEDIA_CHOICES = (
    ('Audio', (
        ('vinyl', 'Vinyl'),
        ('cd', 'CD'),
    )
    ),
    ('Video', (
        ('vhs', 'VHS Tape'),
        ('dvd', 'DVD'),
    )
    ),
    ('unknown', 'Unknown'),
)


class ContactForm(TestForm):
    pass


class ContactBaseFormSet(BaseFormSet):
    def add_fields(self, form, index):
        super(ContactBaseFormSet, self).add_fields(form, index)

    def clean(self):
        super(ContactBaseFormSet, self).clean()
        raise forms.ValidationError("This error was added to show the non form"
                                    " errors styling")

ContactFormSet = formset_factory(TestForm, formset=ContactBaseFormSet,
                                 extra=2,
                                 max_num=4,
                                 validate_max=True)


class FilesForm(forms.Form):
    text1 = forms.CharField()
    file1 = forms.FileField()
    file2 = forms.FileField(required=False)
    file3 = forms.FileField(widget=forms.ClearableFileInput)
    file4 = forms.FileField(required=False, widget=forms.ClearableFileInput)


class MeetingForm(forms.Form):
    mettype = forms.CharField()
    desc = forms.CharField()
    support = forms.CharField()
    date = forms.DateTimeField(
        required=True,
        widget=DateTimeWidget(attrs={'id': "yourdatetimeid"}, usel10n=True,
                              bootstrap_version=3))


class QueryForm(forms.Form):
    need = forms.CharField()
    date = forms.DateTimeField(
        required=True,
        widget=DateTimeWidget(attrs={'id': "yourdatetimeid"}, usel10n=True,
                              bootstrap_version=3))
    duration = forms.CharField()
    description = forms.CharField()


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()

    def clean(self):
        cleaned_data = super(ArticleForm, self).clean()
        raise forms.ValidationError("This error was added to show the non"
                                    " field errors styling.")
        return cleaned_data
