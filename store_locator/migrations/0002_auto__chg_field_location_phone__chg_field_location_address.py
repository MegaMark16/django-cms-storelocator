# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Location.phone'
        db.alter_column('store_locator_location', 'phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Location.address'
        db.alter_column('store_locator_location', 'address', self.gf('django.db.models.fields.TextField')(max_length=255))


    def backwards(self, orm):
        
        # Changing field 'Location.phone'
        db.alter_column('store_locator_location', 'phone', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Location.address'
        db.alter_column('store_locator_location', 'address', self.gf('django.db.models.fields.CharField')(max_length=255))


    models = {
        'store_locator.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['store_locator']
