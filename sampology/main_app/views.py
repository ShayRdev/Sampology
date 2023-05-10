from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Song

# Create your views here.

def home(request):
    return render(request, 'home.html')

def songs_index(request):
    songs = Song.objects.all()
    return render(request, 'songs/index.html', { 
        'songs': songs
     })

class SongDetail(DetailView):
    model = Song

class SongCreate(CreateView):
    model = Song
    fields = '__all__'

class SongUpdate(UpdateView):
    model = Song
    fields = ['release_date']

class SongDelete(DeleteView):
    model = Song
    success_url = '/songs'