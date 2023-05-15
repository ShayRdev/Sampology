from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Gear(models.Model):
    gear_name = models.CharField(max_length=100)
    gear_brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    release_year = models.IntegerField()

    def __str__(self):
        return self.gear_name
    
    def get_absolute_url(self):
        return reverse("gears_detail", kwargs={'pk': self.id})
    

class Song(models.Model):
    artist = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    gear_used = models.ManyToManyField(Gear)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index")
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
    
    def get_absolute_url(self):
        return reverse("home")
    