from django.contrib import admin

# Register your models here.
from webapp.models import User, Post, Movie

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Movie)