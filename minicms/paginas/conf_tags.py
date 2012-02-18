# -*- coding: utf-8 -*-
'''
    minicms

    Desarrollado por Lastchance SL
    web: www.lastchance.es
'''

from django.template import Library, Node
from django.db.models import get_model
from paginas.models import *

register = Library()

class ConfDatos(Node):
    def render(self, context):
        context['conf_list'] = Configuracion.on_site.all()
        return ''

def conf_list(parser, token):
    """
    Para acceder al tag llamar en la plantilla a {% get_conf_list %}
    """
    return ConfDatos()

register.tag('get_conf_list', conf_list)