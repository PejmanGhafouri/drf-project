from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=100, unique=True)
	author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	content = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)
	
	def __str__(self):
		return self.title
