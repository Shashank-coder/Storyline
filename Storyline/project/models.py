from django.db import models
from account.models import CustomUser

# Create your models here.

class story(models.Model):
	name = models.CharField(max_length = 50)
	theme = models.CharField(max_length = 100)
	idea = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)    
	by = models.ForeignKey(CustomUser, related_name = 'story_creator')
	followers = models.ManyToManyField(CustomUser, related_name = 'story_followers')
	def __str__(self):
		return self.name

class chapter(models.Model):
	name = models.CharField(max_length = 50)
	theme = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
	by = models.ForeignKey(CustomUser, related_name = 'Contributor')
	#freezingtime
	content = models.TextField()
	story = models.ForeignKey(story, related_name = 'story')
	followers = models.ManyToManyField(CustomUser, related_name = 'chapter_followers')
	def __str__(self):
		return self.name

class comments(models.Model):
	text = models.CharField(max_length = 1000)
	commented_at = models.DateTimeField(auto_now_add = True)
	commented_by = models.ForeignKey(CustomUser, related_name = 'Commented_by')
	story = models.ForeignKey(story, related_name = 'comment_on_story')
	chapter = models.ForeignKey(chapter, related_name = 'comment_on_chapter')
	liked_by = models.ManyToManyField(CustomUser, related_name = 'liked_by')
	def __str__(self):
		return self.text[:20];

