# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sounds'
        db.create_table(u'api_sounds', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('xenocanto_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('species_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('waveform_path', self.gf('django.db.models.fields.FilePathField')(path=None, max_length=100)),
            ('spectrogram_path', self.gf('django.db.models.fields.FilePathField')(path=None, max_length=100)),
            ('added_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Sounds'])


    def backwards(self, orm):
        # Deleting model 'Sounds'
        db.delete_table(u'api_sounds')


    models = {
        u'api.sounds': {
            'Meta': {'ordering': "('added_date',)", 'object_name': 'Sounds'},
            'added_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'species_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'spectrogram_path': ('django.db.models.fields.FilePathField', [], {'path': 'None', 'max_length': '100'}),
            'waveform_path': ('django.db.models.fields.FilePathField', [], {'path': 'None', 'max_length': '100'}),
            'xenocanto_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['api']