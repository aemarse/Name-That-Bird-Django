# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sounds.xc_id'
        db.add_column(u'api_sounds', 'xc_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sounds.xc_id'
        db.delete_column(u'api_sounds', 'xc_id')


    models = {
        u'api.annotations': {
            'Meta': {'ordering': "('added_date',)", 'object_name': 'Annotations'},
            'added_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sound': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'annotations'", 'to': u"orm['api.Sounds']"}),
            'spec_offset': ('django.db.models.fields.FloatField', [], {}),
            'spec_onset': ('django.db.models.fields.FloatField', [], {}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ann-species'", 'to': u"orm['api.Species']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'annotations'", 'to': u"orm['auth.User']"}),
            'wave_offset': ('django.db.models.fields.FloatField', [], {}),
            'wave_onset': ('django.db.models.fields.FloatField', [], {})
        },
        u'api.groundtruth': {
            'Meta': {'object_name': 'GroundTruth'},
            'added_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sound': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'truth'", 'to': u"orm['api.Sounds']"}),
            'spec_offset': ('django.db.models.fields.FloatField', [], {}),
            'spec_onset': ('django.db.models.fields.FloatField', [], {}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'truth-species'", 'to': u"orm['api.Species']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'truth'", 'to': u"orm['auth.User']"}),
            'wave_offset': ('django.db.models.fields.FloatField', [], {}),
            'wave_onset': ('django.db.models.fields.FloatField', [], {})
        },
        u'api.lessons': {
            'Meta': {'object_name': 'Lessons'},
            'added_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'playlist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lessons'", 'to': u"orm['api.Playlists']"})
        },
        u'api.playlists': {
            'Meta': {'object_name': 'Playlists'},
            'added_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'playlist_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'playlist_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'playlist-type'", 'to': u"orm['api.PlaylistTypes']"})
        },
        u'api.playlisttypes': {
            'Meta': {'object_name': 'PlaylistTypes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'playlist_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'api.sounds': {
            'Meta': {'ordering': "('added_date',)", 'object_name': 'Sounds'},
            'added_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lessons': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sounds'", 'symmetrical': 'False', 'to': u"orm['api.Lessons']"}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sp'", 'to': u"orm['api.Species']"}),
            'spectrogram_path': ('django.db.models.fields.FilePathField', [], {'path': 'None', 'max_length': '100'}),
            'waveform_path': ('django.db.models.fields.FilePathField', [], {'path': 'None', 'max_length': '100'}),
            'xc_id': ('django.db.models.fields.IntegerField', [], {}),
            'xenocanto_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'api.species': {
            'Meta': {'object_name': 'Species'},
            'eng_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['api']