# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'FlickrPhoto.square_url'
        db.add_column('flickrimporter_flickrphoto', 'square_url', self.gf('django.db.models.fields.URLField')(default='', max_length=200), keep_default=False)

        # Adding field 'FlickrPhoto.thumbnail_url'
        db.add_column('flickrimporter_flickrphoto', 'thumbnail_url', self.gf('django.db.models.fields.URLField')(default='', max_length=200), keep_default=False)

        # Adding field 'FlickrPhoto.small_url'
        db.add_column('flickrimporter_flickrphoto', 'small_url', self.gf('django.db.models.fields.URLField')(default='', max_length=200), keep_default=False)

        # Adding field 'FlickrPhoto.medium_url'
        db.add_column('flickrimporter_flickrphoto', 'medium_url', self.gf('django.db.models.fields.URLField')(default='', max_length=200), keep_default=False)

        # Adding field 'FlickrPhoto.original_url'
        db.add_column('flickrimporter_flickrphoto', 'original_url', self.gf('django.db.models.fields.URLField')(default='', max_length=200), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'FlickrPhoto.square_url'
        db.delete_column('flickrimporter_flickrphoto', 'square_url')

        # Deleting field 'FlickrPhoto.thumbnail_url'
        db.delete_column('flickrimporter_flickrphoto', 'thumbnail_url')

        # Deleting field 'FlickrPhoto.small_url'
        db.delete_column('flickrimporter_flickrphoto', 'small_url')

        # Deleting field 'FlickrPhoto.medium_url'
        db.delete_column('flickrimporter_flickrphoto', 'medium_url')

        # Deleting field 'FlickrPhoto.original_url'
        db.delete_column('flickrimporter_flickrphoto', 'original_url')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'flickrimporter.flickrphoto': {
            'Meta': {'object_name': 'FlickrPhoto'},
            'farm': ('django.db.models.fields.IntegerField', [], {}),
            'flickr_id': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'original_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flickrimporter.FlickrUser']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'server': ('django.db.models.fields.IntegerField', [], {}),
            'small_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'square_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'subdomain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['subdomains.Subdomain']"}),
            'thumbnail_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'flickrimporter.flickruser': {
            'Meta': {'object_name': 'FlickrUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nsid': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'token': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'subdomains.subdomain': {
            'Meta': {'object_name': 'Subdomain'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subdomain_text': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['flickrimporter']
