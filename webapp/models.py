from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
	""" User Model """
	username = models.CharField(max_length=50, primary_key=True)
	password = models.CharField(max_length=200)
	email = models.EmailField(unique=True)

	def __str__(self):
		return self.username


class Movie(models.Model):
	""" Movie Model """
	m_id = models.PositiveIntegerField(primary_key=True)
	title = models.CharField(max_length=100)
	poster_path = models.CharField(max_length=100)
	release_date = models.CharField(max_length=10, null=True)

	''' to be added later

	director = models.CharField(max_length=100)
	genre = models.CharField(max_length=50)
	runtime = models.PositiveIntegerField()

	'''


class Post(models.Model):
	""" Post Model """
	m_id = models.ForeignKey('Movie', db_column="m_id", on_delete=models.CASCADE)
	username = models.ForeignKey('User', db_column="username", on_delete=models.CASCADE)
	rating = models.FloatField()
	review = models.TextField(null=True)
