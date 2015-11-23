# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'TwitterPlugin.count'
        db.delete_column('cmsplugin_twitterplugin', 'count')

        # Deleting field 'TwitterPlugin.username'
        db.delete_column('cmsplugin_twitterplugin', 'username')

        # Deleting field 'TwitterPlugin.title'
        db.delete_column('cmsplugin_twitterplugin', 'title')

        # Deleting field 'TwitterPlugin.query'
        db.delete_column('cmsplugin_twitterplugin', 'query')

        # Adding field 'TwitterPlugin.widget_id'
        db.add_column('cmsplugin_twitterplugin', 'widget_id',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=75),
                      keep_default=False)

        # Adding field 'TwitterPlugin.href'
        db.add_column('cmsplugin_twitterplugin', 'href',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=75, blank=True),
                      keep_default=False)

        # Adding field 'TwitterPlugin.link_title'
        db.add_column('cmsplugin_twitterplugin', 'link_title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=75, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'TwitterPlugin.count'
        db.add_column('cmsplugin_twitterplugin', 'count',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=3),
                      keep_default=False)

        # Adding field 'TwitterPlugin.username'
        db.add_column('cmsplugin_twitterplugin', 'username',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'TwitterPlugin.title'
        db.add_column('cmsplugin_twitterplugin', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=75, blank=True),
                      keep_default=False)

        # Adding field 'TwitterPlugin.query'
        db.add_column('cmsplugin_twitterplugin', 'query',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Deleting field 'TwitterPlugin.widget_id'
        db.delete_column('cmsplugin_twitterplugin', 'widget_id')

        # Deleting field 'TwitterPlugin.href'
        db.delete_column('cmsplugin_twitterplugin', 'href')

        # Deleting field 'TwitterPlugin.link_title'
        db.delete_column('cmsplugin_twitterplugin', 'link_title')


    models = {
        'aldryn_twitter.twitterplugin': {
            'Meta': {'object_name': 'TwitterPlugin', 'db_table': "'cmsplugin_twitterplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'href': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'link_title': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'widget_id': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['aldryn_twitter']