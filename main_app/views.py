from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .models import Gear, Song, Post
from django.contrib.auth import login
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def home(request):
    post = Post.objects.all()
    posts_form = PostForm()
    return render(request, 'home.html', {
        'post': post,
        'posts_form': posts_form,
    })

@login_required
def songs_index(request):
    songs = Song.objects.all()
    return render(request, 'songs/index.html', { 
        'songs': songs
     })

@login_required
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
    fields = ['artist', 'name', 'release_date',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SongUpdate(LoginRequiredMixin, UpdateView):
    model = Song
    fields = ['release_date']

class SongDelete(LoginRequiredMixin, DeleteView):
    model = Song
    success_url = '/songs'

class GearList(LoginRequiredMixin, ListView):
    model = Gear

class GearDetail(LoginRequiredMixin, DetailView):
    model = Gear

class GearCreate(LoginRequiredMixin, CreateView):
    model = Gear
    fields = '__all__'

@login_required
def assoc_gear(request, song_id, gear_id):
    Song.objects.get(id=song_id).gear_used.add(gear_id)
    return redirect('songs_detail', song_id=song_id)

@login_required
def unassoc_gear(request, song_id, gear_id):
    Song.objects.get(id=song_id).gear_used.remove(gear_id)
    return redirect('songs_detail', song_id=song_id)

@login_required
def create_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.user = request.user
        new_post.save()
    return redirect('home')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)