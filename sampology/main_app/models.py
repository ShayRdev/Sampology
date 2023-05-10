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
    