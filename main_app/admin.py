from django.contrib import admin
from .models import Song, Gear, Post
# Register your models here.

admin.site.register(Song)
admin.site.register(Gear)
admin.site.register(Post)