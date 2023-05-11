from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .models import Gear, Song

# Create your views here.

def home(request):
    return render(request, 'home.html')

def songs_index(request):
    songs = Song.objects.all()
    return render(request, 'songs/index.html', { 
        'songs': songs
     })

def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    id_list = song.gear_used.all().values_list('id')
    gear_used_song_doesnt_have = Gear.objects.exclude(id__in=id_list)
    return render(request, 'main_app/song_detail.html', {
        'song': song,
        'gear_used': gear_used_song_doesnt_have
    })


class SongCreate(CreateView):
    model = Song
    fields = '__all__'

class SongUpdate(UpdateView):
    model = Song
    fields = ['release_date']

class SongDelete(DeleteView):
    model = Song
    success_url = '/songs'

class GearList(ListView):
    model = Gear

class GearDetail(DetailView):
    model = Gear

class GearCreate(CreateView):
    model = Gear
    fields = '__all__'

def assoc_gear(request, song_id, gear_id):
    Song.objects.get(id=song_id).gear_used.add(gear_id)
    return redirect('songs_detail', song_id=song_id)

def unassoc_gear(request, song_id, gear_id):
    Song.objects.get(id=song_id).gear_used.remove(gear_id)
    return redirect('songs_detail', song_id=song_id)
