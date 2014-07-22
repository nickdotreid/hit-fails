# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Submission.vendor_id'
        db.delete_column(u'fails_submission', 'vendor_id_id')

        # Adding field 'Submission.vendor'
        db.add_column(u'fails_submission', 'vendor',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fails.Vendor'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'Submission.location'
        db.alter_column(u'fails_submission', 'location', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Submission.software'
        db.alter_column(u'fails_submission', 'software', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Submission.vendor_id'
        raise RuntimeError("Cannot reverse this migration. 'Submission.vendor_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Submission.vendor_id'
        db.add_column(u'fails_submission', 'vendor_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fails.Vendor']),
                      keep_default=False)

        # Deleting field 'Submission.vendor'
        db.delete_column(u'fails_submission', 'vendor_id')


        # User chose to not deal with backwards NULL issues for 'Submission.location'
        raise RuntimeError("Cannot reverse this migration. 'Submission.location' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Submission.location'
        db.alter_column(u'fails_submission', 'location', self.gf('django.db.models.fields.CharField')(max_length=64))

        # User chose to not deal with backwards NULL issues for 'Submission.software'
        raise RuntimeError("Cannot reverse this migration. 'Submission.software' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Submission.software'
        db.alter_column(u'fails_submission', 'software', self.gf('django.db.models.fields.CharField')(max_length=128))

    models = {
        u'fails.image': {
            'Meta': {'object_name': 'Image'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_path': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'submission_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fails.Submission']"})
        },
        u'fails.submission': {
            'Meta': {'object_name': 'Submission'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'software': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'upvotes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fails.Vendor']", 'null': 'True', 'blank': 'True'})
        },
        u'fails.tag': {
            'Meta': {'ordering': "['tag_text']", 'object_name': 'Tag'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'submissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['fails.Submission']", 'symmetrical': 'False'}),
            'tag_text': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'fails.vendor': {
            'Meta': {'ordering': "['vendor_name']", 'object_name': 'Vendor'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'vendor_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['fails']