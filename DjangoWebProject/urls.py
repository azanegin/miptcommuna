"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import patterns, url

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^meetings$', 'app.views.meetings', name='contact'),
    url(r'^trips', 'app.views.trips', name='about'),
    url(r'^post', 'app.views.post_wanted', name='post'),
    #url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    #url(r'^logout$', 'django.contrib.auth.views.logout',
    #    {
    #        'next_page': '/',
    #    },
    #    name='logout'),

)
