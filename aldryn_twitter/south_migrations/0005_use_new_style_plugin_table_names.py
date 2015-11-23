# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

from django.db import connection, models


class Migration(DataMigration):

    tables = {
        'cmsplugin_twitterplugin': 'aldryn_twitter_twitterplugin',
    }

    def forwards(self, orm):
        table_names = connection.introspection.table_names()
        for old_table, new_table in self.tables.iteritems():
            if old_table in table_names:
                db.rename_table(old_table, new_table)

    def backwards(self, orm):
        table_names = connection.introspection.table_names()
        for old_table, new_table in self.tables.iteritems():
            if new_table in table_names:
                db.rename_table(new_table, old_table)

    models = {
        u'aldryn_twitter.twitterplugin': {
            'Meta': {'object_name': 'TwitterPlugin', '_ormbases': ['cms.CMSPlugin']},
            'aria_politeness': ('django.db.models.fields.CharField', [], {'default': "'polite'", 'max_length': '9'}),
            'border_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'borders': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'footer': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'header': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'href': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'link_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'link_title': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'related_users': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'scrollbar': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'theme': ('django.db.models.fields.CharField', [], {'default': "'light'", 'max_length': '5'}),
            'transparent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tweet_limit': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'widget_id': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['aldryn_twitter']
    symmetrical = True
