from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('songs', views.songs_index, name='index'),
    path('songs/create', views.SongCreate.as_view(), name="songs_create"),
    path("songs/<int:pk>/", views.SongDetail.as_view(), name="songs_detail"),
    path("songs/<int:pk>/update", views.SongUpdate.as_view(), name="songs_update"),
    path("songs/<int:pk>/delete", views.SongDelete.as_view(), name="songs_delete"),
]
