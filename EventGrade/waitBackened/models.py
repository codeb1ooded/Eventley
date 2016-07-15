from __future__ import unicode_literals

from django.db import models

# Create your models here.
class event(models.Model):
	Eventid=models.CharField(max_length=100)
	Eventname=models.CharField(max_length=100)
	Venuename=models.CharField(max_length=100)
	Nolikes=models.IntegerField()
	Category=models.CharField(max_length=100)
	Nocomments=models.IntegerField()
	Nolinks=models.IntegerField()
	#score=no_links+no_comments+no_likes

	def _str_(self):
		return self.event_id + '-' +self.event_name
	

