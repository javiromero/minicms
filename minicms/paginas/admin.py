# -*- coding: utf-8 -*-
'''
    minicms

    Desarrollado por Lastchance SL
    web: www.lastchance.es
'''

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from paginas.models import *
from django.contrib.contenttypes import generic
from django import forms
from django.forms.util import ErrorList


class MetatagInline(generic.GenericStackedInline):
    model       = Metatag
    extra       = 1
    max_num     = 1
    verbose_name = "SEO"

class HomePageModelForm(forms.ModelForm):
    def clean(self):
        if Home.objects.count() > 1:
            self._errors.setdefault('__all__', ErrorList()).append("Ya existe una portada y no se pueden crear más. Edita la existente.")
        return self.cleaned_data

class HomeAdmin(admin.ModelAdmin):
    list_display        = ('titulo', 'site', 'status',)
    search_fields       = ('titulo',)
    ordering    = ('site',)
    fieldsets   = [
        (None, {'fields': ['titulo', 'status', 'site']}),
        ('Texto', {'fields': ['destacado', 'contenido1', 'contenido2', 'contenido3', 'contenido4', 'contenido5', 'precios']}),
        ('Formulario', {'fields': ['titulo_form', 'boton_form']}),
        ('Imagenes', {'fields': ['imagen_cabecera', 'imagen_cuerpo']}),
        ('Mapa', {'fields': ['google_maps_coords', 'google_maps_zoom']}),
    ]

    inlines = [
        MetatagInline,
    ]

    class Media:
        js = ('/estaticos/js/tiny_mce/tiny_mce.js',
              '/estaticos/js/editores/editores.js',)

class PageAdmin(admin.ModelAdmin):
    list_display        = ('titulo', 'sites', 'status',)
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields       = ('titulo',)
    ordering    = ('sites',)
    fieldsets   = [
        (None, {'fields': ['titulo', 'slug', 'status', 'sites']}),
        ('Texto', {'fields': ['contenido']}),
    ]

    inlines = [
        MetatagInline,
    ]

    class Media:
        js = ('/estaticos/js/tiny_mce/tiny_mce.js',
              '/estaticos/js/editores/editores.js')

class NotificationEmailInline(admin.StackedInline):
    model       = NotificationEmail
    extra       = 1
    verbose_name = _(u'Correos electrónicos a los que notificar')

class ConfiguracionAdmin(admin.ModelAdmin):
    list_display        = ('site',)
    ordering    = ('site',)
    fieldsets   = [
        (None, {'fields': ['site']}),
        ('Dirección Postal', {'fields': ['telefono', 'direccion', 'codigo_postal', 'ciudad']}),
        ('Codigos', {'fields': ['google_analytics', 'verificacion_webmaster']}),
        ('Imagenes', {'fields': ['logo']}),
        ('Colores', {'fields': ['color_principal', 'color_secundario']}),
    ]
    
    inlines     = [
        NotificationEmailInline,
    ]
    
    class Media:
        css = {
            'all': ('/estaticos/css/jquery.miniColors.css',)
        }
        js = ('/estaticos/js/jquery.miniColors.js',
              '/estaticos/js/functions.js',)

admin.site.register(Home, HomeAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Configuracion, ConfiguracionAdmin)