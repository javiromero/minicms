# -*- coding: utf-8 -*-
'''
    minicms

    Desarrollado por Lastchance SL
    web: www.lastchance.es
'''

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()
   
urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
    # Easy way to check error templates on development
    urlpatterns += patterns('',
        (r'^404/$', direct_to_template, {'template': '404.html'} ),
        (r'^500/$', direct_to_template, {'template': '500.html'} ),
        (r'^503/$', direct_to_template, {'template': '503.html'} ),
    )

urlpatterns += patterns('',
    (r'^', include('paginas.urls')),
)