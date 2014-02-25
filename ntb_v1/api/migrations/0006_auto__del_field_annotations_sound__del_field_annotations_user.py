# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Annotations.sound'
        db.delete_column(u'api_annotations', 'sound_id')

        # Deleting field 'Annotations.user'
        db.delete_column(u'api_annotations', 'user_id')


    def backwards(self, orm):
        # Adding field 'Annotations.sound'
        db.add_column(u'api_annotations', 'sound',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='annotations', to=orm['api.Sounds']),
                      keep_default=False)

        # Adding field 'Annotations.user'
        db.add_column(u'api_annotations', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='annotations', to=orm['auth.User']),
                      keep_default=False)


    models = {
        u'api.annotations': {
            'Meta': {'ordering': "('added_date',)", 'object_name': 'Annotations'},
            'added_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spec_offset': ('django.db.models.fields.FloatField', [], {}),
            'spec_onset': ('django.db.models.fields.FloatField', [], {}),
            'species': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'wave_offset': ('django.db.models.fields.FloatField', [], {}),
            'wave_onset': ('django.db.models.fields.FloatField', [], {})
        },
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