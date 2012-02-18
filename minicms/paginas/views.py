# -*- coding: utf-8 -*-
'''
    minicms

    Desarrollado por Lastchance SL
    web: www.lastchance.es
'''

from django.conf import settings
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response, get_object_or_404
from django import template
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from paginas.models import *

template.add_to_builtins('paginas.activo')
template.add_to_builtins('paginas.conf_tags')

def index(request):
    """
    Vista para home
    """
    items       = Home.on_site.get(status='p')
    mark_type   = ContentType.objects.get_for_model(items)
    metas       = Metatag.objects.filter(content_type__pk=mark_type.id, object_id=items.id)
    site        = Site.objects.get_current()
    
    return render_to_response("paginas/index.html",
                            {
                                'items' : items,
                                'metas' : metas,
                                'site'  : site,
                            },
                            context_instance = RequestContext(request))

def page(request, slug):
    """
    Vista de detalle
    """
    page        = get_object_or_404(Page, slug__exact=slug, sites__id__exact=settings.SITE_ID)
    mark_type   = ContentType.objects.get_for_model(page)
    metas       = Metatag.objects.filter(content_type__pk=mark_type.id, object_id=page.id)

    return render_to_response("paginas/paginas_detail.html",
                                {
                                    'object'    : page,
                                    'metas'     : metas,
                                },
                                context_instance = RequestContext(request))

"""
  Cache for 15 min. as pages won't usually change
"""
index = cache_page(index, 60 * 15)
