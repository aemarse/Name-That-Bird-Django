# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Species'
        db.create_table(u'api_species', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('eng_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'api', ['Species'])

        # Adding model 'GroundTruth'
        db.create_table(u'api_groundtruth', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sound', self.gf('django.db.models.fields.related.ForeignKey')(related_name='anno', to=orm['api.Sounds'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='anno', to=orm['auth.User'])),
            ('wave_onset', self.gf('django.db.models.fields.FloatField')()),
            ('wave_offset', self.gf('django.db.models.fields.FloatField')()),
            ('spec_onset', self.gf('django.db.models.fields.FloatField')()),
            ('spec_offset', self.gf('django.db.models.fields.FloatField')()),
            ('species', self.gf('django.db.models.fields.related.ForeignKey')(related_name='species', to=orm['api.Species'])),
            ('added_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['GroundTruth'])

        # Adding model 'Lessons'
        db.create_table(u'api_lessons', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('playlist', self.gf('django.db.models.fields.related.ForeignKey')(related_name='lessons', to=orm['api.Playlists'])),
            ('added_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Lessons'])

        # Adding model 'Playlists'
        db.create_table(u'api_playlists', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('playlist_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('playlist_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('added_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Playlists'])

        # Adding field 'Sounds.species'
        db.add_column(u'api_sounds', 'species',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='sp', to=orm['api.Species']),
                      keep_default=False)

        # Adding M2M table for field lessons on 'Sounds'
        m2m_table_name = db.shorten_name(u'api_sounds_lessons')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sounds', models.ForeignKey(orm[u'api.sounds'], null=False)),
            ('lessons', models.ForeignKey(orm[u'api.lessons'], null=False))
        ))
        db.create_unique(m2m_table_name, ['sounds_id', 'lessons_id'])


    def backwards(self, orm):
        # Deleting model 'Species'
        db.delete_table(u'api_species')

        # Deleting model 'GroundTruth'
        db.delete_table(u'api_groundtruth')

        # Deleting model 'Lessons'
        db.delete_table(u'api_lessons')

        # Deleting model 'Playlists'
        db.delete_table(u'api_playlists')

        # Deleting field 'Sounds.species'
        db.delete_column(u'api_sounds', 'species_id')

        # Removing M2M table for field lessons on 'Sounds'
        db.delete_table(db.shorten_name(u'api_sounds_lessons'))


    models = {
        u'api.annotations': {
            'Meta': {'ordering': "('added_date',)", 'object_name': 'Annotations'},
            'added_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sound': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'annotations'", 'to': u"orm['api.Sounds']"}),
            'spec_offset': ('django.db.models.fields.FloatField', [], {}),
            'spec_onset': ('django.db.models.fields.FloatField', [], {}),
            'species': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'annotations'", 'to': u"orm['auth.User']"}),
            'wave_offset': ('django.db.models.fields.FloatField', [], {}),
            'wave_onset': ('django.db.models.fields.FloatField', [], {})
        },
        u'api.groundtruth': {
            'Meta': {'object_name': 'GroundTruth'},
            'added_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sound': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'anno'", 'to': u"orm['api.Sounds']"}),
            'spec_offset': ('django.db.models.fields.FloatField', [], {}),
            'spec_onset': ('django.db.models.fields.FloatField', [], {}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'species'", 'to': u"orm['api.Species']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'anno'", 'to': u"orm['auth.User']"}),
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
            'playlist_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'api.sounds': {
            'Meta': {'ordering': "('added_date',)", 'object_name': 'Sounds'},
            'added_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lessons': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lessons'", 'symmetrical': 'False', 'to': u"orm['api.Lessons']"}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sp'", 'to': u"orm['api.Species']"}),
            'species_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'spectrogram_path': ('django.db.models.fields.FilePathField', [], {'path': 'None', 'max_length': '100'}),
            'waveform_path': ('django.db.models.fields.FilePathField', [], {'path': 'None', 'max_length': '100'}),
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