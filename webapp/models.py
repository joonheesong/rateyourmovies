from django.db import models
from django.utils import timezone

# Create your models here.

class Users(models.Model):
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
	poster_path = models.CharField(max_length=100, null=True)
	release_date = models.CharField(max_length=10, null=True)

	''' to be added later

	director = models.CharField(max_length=100)
	genre = models.CharField(max_length=50)
	runtime = models.PositiveIntegerField()

	'''
	def __str__(self):
		return self.title + "\nID: " + str(self.m_id) + "\nRelease Date: " + self.release_date

class Posting(models.Model):
	""" Post Model """
	m_id = models.ForeignKey('Movie', db_column="m_id", on_delete=models.CASCADE)
	username = models.ForeignKey('Users', db_column="username", on_delete=models.CASCADE)
	rating = models.FloatField(null=True)
	review = models.TextField(null=True)

	def new_review(self, new_review):
		self.review = new_review