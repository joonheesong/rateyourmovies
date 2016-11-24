from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=50, primary_key=True)
	password = models.CharField(max_length=200)
	email = models.EmailField()

	def set_password(self, pw):
		password = pw

	def __str__(self):
		return self.username

'''
class Movie(models.Model):
	m_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100)
	director = models.CharField(max_length=100)
	genre = models.CharField(max_length=50)
	runtime = models.PositiveIntegerField()
	poster = models.ImageField()
	published_year = models.PositiveIntegerField()


class Post(models.Model):
	m_id = models.ForeignKey('Movie.m_id')
	username = models.ForeignKey('User.username')
	rating = models.FloatField()
'''