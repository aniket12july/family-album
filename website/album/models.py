from django.db import models

class Event(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	event_time = models.DateTimeField()
	
	def __unicode__(self):
		return self.title
	
class Photo(models.Model):
	event = models.ForeignKey(Event)
	title = models.CharField(max_length=200)
	description = models.TextField()
	path = models.ImageField(upload_to='unsorted')
	
	def __unicode_(self):
		return self.title
