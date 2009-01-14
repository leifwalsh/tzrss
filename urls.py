from django.conf.urls.defaults import *

import os

from tzrss import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Example:
    # (r'^tzrss/', include('tzrss.foo.urls')),
    (r'^convert/?$', 'tzrss.morningbell.views.convert'),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': os.path.join(settings.BASE_DIR, 'css')}),
    (r'^img/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': os.path.join(settings.BASE_DIR, 'img')}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': os.path.join(settings.BASE_DIR, 'js')}),
    (r'^/?$', 'tzrss.morningbell.views.index'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
