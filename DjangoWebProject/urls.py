"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import patterns, url

from app.views import *

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^formset$', DefaultFormsetView.as_view(), name='formset_default'),
    url(r'^form$', DefaultFormView.as_view(), name='form_default'),
    url(r'^form_by_field$', DefaultFormByFieldView.as_view(), name='form_by_field'),
    url(r'^form_horizontal$', FormHorizontalView.as_view(), name='form_horizontal'),
    url(r'^form_inline$', FormInlineView.as_view(), name='form_inline'),
    url(r'^form_with_files$', FormWithFilesView.as_view(), name='form_with_files'),
    url(r'^pagination$', PaginationView.as_view(), name='pagination'),
    url(r'^misc$', MiscView.as_view(), name='misc'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^meetings$', 'app.views.meetings', name='contact'),
    url(r'^person/(?P<person_id>\d+)/$', 'app.views.person', name='person_page'),
    url(r'^item/(?P<item_id>\d+)/$', 'app.views.item', name='item_page'),
    url(r'^trips', 'app.views.trips', name='about'),
    url(r'^post_meeting', MeetingFormView.as_view(), name='form_meeting'),
    # url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^logout$', 'django.contrib.auth.views.logout',
    #    {
    #        'next_page': '/',
    #    },
    #    name='logout'),

)
