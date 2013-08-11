from django.db import models
from time import time
import os.path
from django_test import settings

def get_upload_file_name(instance, filename):
	return settings.UPLOAD_FILE_PATTERN(% (str(time()).replace('.','_'), filename)

class Article(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField(default=0)
	thumbnail = models.FileField(upload_to=get_upload_file_name, blank=True, null=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/articles/get/%i/" % self.id

	def get_thumbnail(self):
		thumb = str(self.thumbnail)
		if not setting.DEBUG:
			thumb = thumb.replace('assets/', '')
			
		return thumb

class Comment(models.Model):
	name = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	article = models.ForeignKey(Article)

		
