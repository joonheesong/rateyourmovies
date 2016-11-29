from django.contrib import admin

# Register your models here.
from webapp.models import Users,Posting, Movie

admin.site.register(Users)
admin.site.register(Posting)
admin.site.register(Movie)