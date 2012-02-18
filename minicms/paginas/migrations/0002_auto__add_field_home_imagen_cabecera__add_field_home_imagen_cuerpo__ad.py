# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Home.imagen_cabecera'
        db.add_column('paginas_home', 'imagen_cabecera', self.gf('sorl.thumbnail.fields.ImageField')(default='cabeceras/default.gif', max_length=100), keep_default=False)

        # Adding field 'Home.imagen_cuerpo'
        db.add_column('paginas_home', 'imagen_cuerpo', self.gf('sorl.thumbnail.fields.ImageField')(default='cuerpos/default.gif', max_length=100), keep_default=False)

        # Adding field 'Home.google_maps_coords'
        db.add_column('paginas_home', 'google_maps_coords', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Home.google_maps_zoom'
        db.add_column('paginas_home', 'google_maps_zoom', self.gf('django.db.models.fields.IntegerField')(default=5, blank=True), keep_default=False)

        # Adding field 'Configuracion.logo'
        db.add_column('paginas_configuracion', 'logo', self.gf('sorl.thumbnail.fields.ImageField')(default='logos/default.gif', max_length=100), keep_default=False)

        # Adding field 'Configuracion.color_principal'
        db.add_column('paginas_configuracion', 'color_principal', self.gf('django.db.models.fields.CharField')(default='#1122CC', max_length=7), keep_default=False)

        # Adding field 'Configuracion.color_secundario'
        db.add_column('paginas_configuracion', 'color_secundario', self.gf('django.db.models.fields.CharField')(default='#F1F1F1', max_length=7), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Home.imagen_cabecera'
        db.delete_column('paginas_home', 'imagen_cabecera')

        # Deleting field 'Home.imagen_cuerpo'
        db.delete_column('paginas_home', 'imagen_cuerpo')

        # Deleting field 'Home.google_maps_coords'
        db.delete_column('paginas_home', 'google_maps_coords')

        # Deleting field 'Home.google_maps_zoom'
        db.delete_column('paginas_home', 'google_maps_zoom')

        # Deleting field 'Configuracion.logo'
        db.delete_column('paginas_configuracion', 'logo')

        # Deleting field 'Configuracion.color_principal'
        db.delete_column('paginas_configuracion', 'color_principal')

        # Deleting field 'Configuracion.color_secundario'
        db.delete_column('paginas_configuracion', 'color_secundario')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'paginas.configuracion': {
            'Meta': {'object_name': 'Configuracion'},
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'color_principal': ('django.db.models.fields.CharField', [], {'default': "'#1122CC'", 'max_length': '7'}),
            'color_secundario': ('django.db.models.fields.CharField', [], {'default': "'#F1F1F1'", 'max_length': '7'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'google_analytics': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('sorl.thumbnail.fields.ImageField', [], {'default': "'logos/default.gif'", 'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']", 'unique': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'verificacion_webmaster': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'paginas.home': {
            'Meta': {'ordering': "['site']", 'object_name': 'Home'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'destacado': ('django.db.models.fields.TextField', [], {}),
            'google_maps_coords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'google_maps_zoom': ('django.db.models.fields.IntegerField', [], {'default': '5', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen_cabecera': ('sorl.thumbnail.fields.ImageField', [], {'default': "'cabeceras/default.gif'", 'max_length': '100'}),
            'imagen_cuerpo': ('sorl.thumbnail.fields.ImageField', [], {'default': "'cuerpos/default.gif'", 'max_length': '100'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'publicado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']", 'unique': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'b'", 'max_length': '1'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        'paginas.metatag': {
            'Meta': {'object_name': 'Metatag'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'palabras_clave': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'robots': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '2'})
        },
        'paginas.page': {
            'Meta': {'ordering': "['sites']", 'unique_together': "(['sites', 'slug'],)", 'object_name': 'Page'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'publicado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '120', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'b'", 'max_length': '1'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['paginas']
