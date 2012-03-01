# -*- coding: utf-8 -*-
'''
    minicms

    Desarrollado por Lastchance SL
    web: www.lastchance.es
'''

from django.conf.urls.defaults import *
from paginas.models import *
from paginas.views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index',),
    url(r'^enviar/$', contact, name='contacto'),
    url(r'^(?P<slug>[^/]+)/$', page, name='pagina_detalle'),
)