# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TwitterPlugin.theme'
        db.add_column('cmsplugin_twitterplugin', 'theme',
                      self.gf('django.db.models.fields.CharField')(default='light', max_length=5),
                      keep_default=False)

        # Adding field 'TwitterPlugin.link_color'
        db.add_column('cmsplugin_twitterplugin', 'link_color',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=6, blank=True),
                      keep_default=False)

        # Adding field 'TwitterPlugin.border_color'
        db.add_column('cmsplugin_twitterplugin', 'border_color',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=6, blank=True),
                      keep_default=False)

        # Adding field 'TwitterPlugin.width'
        db.add_column('cmsplugin_twitterplugin', 'width',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'TwitterPlugin.height'
        db.add_column('cmsplugin_twitterplugin', 'height',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'TwitterPlugin.header'
        db.add_column('cmsplugin_twitterplugin', 'header',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'TwitterPlugin.footer'
        db.add_column('cmsplugin_twitterplugin', 'footer',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'TwitterPlugin.borders'
        db.add_column('cmsplugin_twitterplugin', 'borders',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'TwitterPlugin.scrollbar'
        db.add_column('cmsplugin_twitterplugin', 'scrollbar',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'TwitterPlugin.transparent'
        db.add_column('cmsplugin_twitterplugin', 'transparent',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'TwitterPlugin.language_code'
        db.add_column('cmsplugin_twitterplugin', 'language_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True),
                      keep_default=False)

        # Adding field 'TwitterPlugin.tweet_limit'
        db.add_column('cmsplugin_twitterplugin', 'tweet_limit',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'TwitterPlugin.related_users'
        db.add_column('cmsplugin_twitterplugin', 'related_users',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'TwitterPlugin.aria_politeness'
        db.add_column('cmsplugin_twitterplugin', 'aria_politeness',
                      self.gf('django.db.models.fields.CharField')(default='polite', max_length=9),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TwitterPlugin.theme'
        db.delete_column('cmsplugin_twitterplugin', 'theme')

        # Deleting field 'TwitterPlugin.link_color'
        db.delete_column('cmsplugin_twitterplugin', 'link_color')

        # Deleting field 'TwitterPlugin.border_color'
        db.delete_column('cmsplugin_twitterplugin', 'border_color')

        # Deleting field 'TwitterPlugin.width'
        db.delete_column('cmsplugin_twitterplugin', 'width')

        # Deleting field 'TwitterPlugin.height'
        db.delete_column('cmsplugin_twitterplugin', 'height')

        # Deleting field 'TwitterPlugin.header'
        db.delete_column('cmsplugin_twitterplugin', 'header')

        # Deleting field 'TwitterPlugin.footer'
        db.delete_column('cmsplugin_twitterplugin', 'footer')

        # Deleting field 'TwitterPlugin.borders'
        db.delete_column('cmsplugin_twitterplugin', 'borders')

        # Deleting field 'TwitterPlugin.scrollbar'
        db.delete_column('cmsplugin_twitterplugin', 'scrollbar')

        # Deleting field 'TwitterPlugin.transparent'
        db.delete_column('cmsplugin_twitterplugin', 'transparent')

        # Deleting field 'TwitterPlugin.language_code'
        db.delete_column('cmsplugin_twitterplugin', 'language_code')

        # Deleting field 'TwitterPlugin.tweet_limit'
        db.delete_column('cmsplugin_twitterplugin', 'tweet_limit')

        # Deleting field 'TwitterPlugin.related_users'
        db.delete_column('cmsplugin_twitterplugin', 'related_users')

        # Deleting field 'TwitterPlugin.aria_politeness'
        db.delete_column('cmsplugin_twitterplugin', 'aria_politeness')


    models = {
        'aldryn_twitter.twitterplugin': {
            'Meta': {'object_name': 'TwitterPlugin', 'db_table': "'cmsplugin_twitterplugin'", '_ormbases': ['cms.CMSPlugin']},
            'aria_politeness': ('django.db.models.fields.CharField', [], {'default': "'polite'", 'max_length': '9'}),
            'border_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'borders': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'footer': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'header': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'href': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'link_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'link_title': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'related_users': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
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