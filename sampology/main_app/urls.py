from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('songs', views.songs_index, name='index'),
    path('songs/create', views.SongCreate.as_view(), name="songs_create"),
    path("songs/<int:song_id>/", views.song_detail, name="songs_detail"),
    path("songs/<int:pk>/update", views.SongUpdate.as_view(), name="songs_update"),
    path("songs/<int:pk>/delete", views.SongDelete.as_view(), name="songs_delete"),
    path("gear/", views.GearList.as_view(), name="gears_index"),
    path("gear/<int:pk>/", views.GearDetail.as_view(), name="gears_detail"),
    path("gear/create", views.GearCreate.as_view(), name="gears_create"),
    path("songs/<int:song_id>/assoc_gear/<int:gear_id>/", views.assoc_gear, name="assoc_gear"),
]
