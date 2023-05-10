from django.db import models
from django.urls import reverse
# Create your models here.

class Song(models.Model):
    artist = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index")
    
class Gear(models.Model):
    gear_name = models.CharField(max_length=100)
    gear_brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    release_year = models.IntegerField()

    def __str__(self):
        return self.gear_name
    
    def get_absolute_url(self):
        return reverse("gears_detail", kwargs={'pk': self.id})
    