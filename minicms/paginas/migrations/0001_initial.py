# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Metatag'
        db.create_table('paginas_metatag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('robots', self.gf('django.db.models.fields.CharField')(default=0, max_length=2)),
            ('palabras_clave', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('paginas', ['Metatag'])

        # Adding model 'Page'
        db.create_table('paginas_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=120, db_index=True)),
            ('publicado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='b', max_length=1)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('sites', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
        ))
        db.send_create_signal('paginas', ['Page'])

        # Adding unique constraint on 'Page', fields ['sites', 'slug']
        db.create_unique('paginas_page', ['sites_id', 'slug'])

        # Adding model 'Configuracion'
        db.create_table('paginas_configuracion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('slogan', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('google_analytics', self.gf('django.db.models.fields.TextField')(max_length=100, null=True, blank=True)),
            ('verificacion_webmaster', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], unique=True)),
        ))
        db.send_create_signal('paginas', ['Configuracion'])

        # Adding model 'Home'
        db.create_table('paginas_home', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('publicado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='b', max_length=1)),
            ('destacado', self.gf('django.db.models.fields.TextField')()),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], unique=True)),
        ))
        db.send_create_signal('paginas', ['Home'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Page', fields ['sites', 'slug']
        db.delete_unique('paginas_page', ['sites_id', 'slug'])

        # Deleting model 'Metatag'
        db.delete_table('paginas_metatag')

        # Deleting model 'Page'
        db.delete_table('paginas_page')

        # Deleting model 'Configuracion'
        db.delete_table('paginas_configuracion')

        # Deleting model 'Home'
        db.delete_table('paginas_home')


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
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'google_analytics': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']", 'unique': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'verificacion_webmaster': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'paginas.home': {
            'Meta': {'ordering': "['site']", 'object_name': 'Home'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'destacado': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
