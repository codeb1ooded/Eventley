from __future__ import unicode_literals

from django.db import models

# Create your models here.
class event(models.Model):
	event_id=models.CharField(max_length=100),
	event_name=models.CharField(max_length=100),
	venue_name=models.CharField(max_length=100),
	no_likes=models.IntegerField(max_length=100),
	category=models.CharField(max_length=100),
	no_comments=models.IntegerField(max_length=100),
	no_links=models.IntegerField(max_length=100),
	#score=no_links+no_comments+no_likes

	def _str_(self):
		return self.event_id + '-' +self.event_name
	

