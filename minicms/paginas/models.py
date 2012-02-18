# -*- coding: utf-8 -*-
'''
    minicms

    Desarrollado por Lastchance SL
    web: www.lastchance.es
'''


from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from sorl.thumbnail import ImageField

STATUS_CHOICES = (
    ('b', 'Borrador'),
    ('p', 'Publicado'),
   )

ROBOTS_CHOICES = (
    ('0', 'index, follow'),
    ('1', 'noindex, follow'),
)

class Metatag(models.Model):
    """
    Meta Tags
    """
    robots              = models.CharField(max_length=2, choices=ROBOTS_CHOICES, default=0, verbose_name=_(u'meta robots'),help_text=_(u'Por defecto \"index, follow\"'))
    palabras_clave      = models.CharField(max_length=255, blank=True, null=True, verbose_name=_(u'meta keyword'), help_text=_(u'Palabras clave separadas por comas. Relacionado con el texto.'))
    descripcion         = models.CharField(max_length=255, blank=True, null=True, verbose_name=_(u'meta description'), help_text=_(u'Breve descripción. Relacionado con el texto.'))
    content_type        = models.ForeignKey(ContentType)
    object_id           = models.PositiveIntegerField()
    content_object      = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
       return self.palabras_clave

    def pal_kw(self):
        return self.palabras_clave

    def _get_dc(self):
        return self.descripcion

class Page(models.Model):
    """
    Páginas del site
    """
    titulo      = models.CharField(verbose_name=_(u'título'), max_length=120, unique=False,)
    slug        = models.SlugField(max_length=120, verbose_name=_(u'URL'), unique=False)
    publicado   = models.DateTimeField(verbose_name=_(u'fecha de publicación'), editable=False, auto_now_add=True)
    modificado  = models.DateTimeField(verbose_name=_(u'fecha última modificación'), editable=False, auto_now=True)
    status      = models.CharField(max_length=1, choices=STATUS_CHOICES, default='b', verbose_name=_(u'Estado'))

    contenido   = models.TextField(verbose_name=_(u'Contenido'))
    sites       = models.ForeignKey(Site, verbose_name=_(u'Web'))

    metatags    = generic.GenericRelation('Metatag')

    objects     = models.Manager()
    on_site     = CurrentSiteManager()

    class Meta:
        verbose_name    = _(u'Página')
        ordering        = ['sites']
        unique_together = ["sites", "slug"]

    def __unicode__(self):
        return self.titulo

    @models.permalink
    def get_absolute_url(self):
        return ('paginas.views.page', [self.slug])

class Configuracion(models.Model):
    """
    Datos para configuración del sitio
    """
    telefono                    = models.CharField(verbose_name=_(u'teléfono'), max_length=11, blank=True, null=True,)
    slogan                      = models.CharField(blank=True, max_length=100, null=True,)
    direccion                   = models.CharField(verbose_name=_(u'dirección'), max_length=100, blank=True, null=True,)
    codigo_postal               = models.CharField(verbose_name=_(u'código postal'), max_length=100, blank=True, null=True,)
    ciudad                      = models.CharField(verbose_name=_(u'ciudad'), max_length=100, blank=True, null=True,)
    google_analytics            = models.TextField(verbose_name=_(u'Código de Analytics'), max_length=100, blank=True, null=True,)
    verificacion_webmaster      = models.CharField(verbose_name=_(u'Código de webmasters'), max_length=100, blank=True, null=True,)

    # Logotipo
    logo                        = ImageField(verbose_name=_(u'Logo'), upload_to='logos', default='logos/default.gif')
    
    # Colores
    color_principal             = models.CharField(verbose_name=_(u'Color principal'), max_length=7, default="#1122CC", help_text=_(u'Se aplica al fondo de cabecera y enlaces'),)
    color_secundario            = models.CharField(verbose_name=_(u'Color secundario'), max_length=7, default="#F1F1F1", help_text=_(u'Se aplica en el fondo de botones'),)
    
    site                        = models.ForeignKey(Site, verbose_name=_(u'Web'), unique=True)

    objects                     = models.Manager()
    on_site                     = CurrentSiteManager()

    class Meta:
        verbose_name            = _(u'Configuración')
        verbose_name_plural     = _(u'Configuraciones')

class Home(models.Model):
    """
    Portada
    """
    titulo      = models.CharField(verbose_name=_(u'título'), max_length=120, unique=True,)
    publicado   = models.DateTimeField(verbose_name=_(u'fecha de publicación'), editable=False, auto_now_add=True)
    modificado  = models.DateTimeField(verbose_name=_(u'fecha última modificación'), editable=False, auto_now=True)
    status      = models.CharField(max_length=1, choices=STATUS_CHOICES, default='b', verbose_name=_(u'Estado'))

    destacado   = models.TextField(verbose_name=_(u'Titulares'), help_text=_(u'Encabezados junto a la imagen'))
    contenido1  = models.TextField(verbose_name=_(u'Contenido 1'))
    contenido2  = models.TextField(verbose_name=_(u'Contenido 2'))
    contenido3  = models.TextField(verbose_name=_(u'Contenido 3'))
    contenido4  = models.TextField(verbose_name=_(u'Contenido 4'))
    precios     = models.TextField(verbose_name=_(u'Tabla de precios'))
    site        = models.ForeignKey(Site, verbose_name=_(u'Web'), unique=True)
    
    # Imagenes
    imagen_cabecera     = ImageField(verbose_name=_(u'Imagen cabecera'), upload_to='cabeceras', default='cabeceras/default.gif')
    imagen_cuerpo       = ImageField(verbose_name=_(u'Imagen cuerpo'), upload_to='cuerpos', default='cuerpos/default.gif')
    
    # Google Maps
    google_maps_coords  = models.CharField(verbose_name=_(u'Coordenadas'), max_length=255, blank=True, null=True, help_text=_(u'Centrar el mapa de Google en estas coordenadas. Debe ser algo similar a: 40.42186,-3.700333'),)
    google_maps_zoom    = models.IntegerField(verbose_name=_(u'Zoom'), blank=True, default=15, help_text=_(u'Zoom que se aplicará al mapa de Google'),)
    
    metatags    = generic.GenericRelation('Metatag')

    objects     = models.Manager()
    on_site     = CurrentSiteManager()

    class Meta:
        verbose_name    = _(u'Portada')
        ordering        = ['site']
        #unique_together = ["site", "titulo"]

    def __unicode__(self):
        return self.titulo

    @models.permalink
    def get_absolute_url(self):
        return ('paginas.views.page', [self.slug])