# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vendor'
        db.create_table(u'fails_vendor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vendor_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'fails', ['Vendor'])

        # Adding model 'Submission'
        db.create_table(u'fails_submission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('vendor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fails.Vendor'])),
            ('software', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('upvotes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'fails', ['Submission'])

        # Adding model 'Image'
        db.create_table(u'fails_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_path', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('submission_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fails.Submission'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'fails', ['Image'])

        # Adding model 'Tag'
        db.create_table(u'fails_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_text', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'fails', ['Tag'])

        # Adding M2M table for field submissions on 'Tag'
        m2m_table_name = db.shorten_name(u'fails_tag_submissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'fails.tag'], null=False)),
            ('submission', models.ForeignKey(orm[u'fails.submission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'submission_id'])


    def backwards(self, orm):
        # Deleting model 'Vendor'
        db.delete_table(u'fails_vendor')

        # Deleting model 'Submission'
        db.delete_table(u'fails_submission')

        # Deleting model 'Image'
        db.delete_table(u'fails_image')

        # Deleting model 'Tag'
        db.delete_table(u'fails_tag')

        # Removing M2M table for field submissions on 'Tag'
        db.delete_table(db.shorten_name(u'fails_tag_submissions'))


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
            'location': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'software': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'upvotes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vendor_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fails.Vendor']"})
        },
        u'fails.tag': {
            'Meta': {'object_name': 'Tag'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'submissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['fails.Submission']", 'symmetrical': 'False'}),
            'tag_text': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'fails.vendor': {
            'Meta': {'object_name': 'Vendor'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'vendor_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['fails']