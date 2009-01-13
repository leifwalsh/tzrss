from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^tzrss/', include('tzrss.foo.urls')),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': '/home/leif/git/tzrss/css'}),
    (r'^img/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': '/home/leif/git/tzrss/img'}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': '/home/leif/git/tzrss/js'}),
    (r'^/?$', 'tzrss.morningbell.views.index'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
