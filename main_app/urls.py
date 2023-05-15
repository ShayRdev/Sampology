from django.urls import path
from . import views

urlpatterns = [
    path('home/create_post/', views.create_post, name="create_post"),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('home/<int:post_id>/', views.home_detail, name="post_detail"),
    path('songs/create', views.SongCreate.as_view(), name="songs_create"),
    path("songs/<int:song_id>/", views.song_detail, name="songs_detail"),
    path("songs/<int:pk>/update", views.SongUpdate.as_view(), name="songs_update"),
    path("songs/<int:pk>/delete", views.SongDelete.as_view(), name="songs_delete"),
    path("songs/<int:song_id>/assoc_gear/<int:gear_id>/", views.assoc_gear, name="assoc_gear"),
    path("songs/<int:song_id>/unassoc_gear/<int:gear_id>/", views.unassoc_gear, name="unassoc_gear"),
    path('songs', views.songs_index, name='index'),
    path("gear/<int:pk>/", views.GearDetail.as_view(), name="gears_detail"),
    path("gear/create", views.GearCreate.as_view(), name="gears_create"),
    path("gear/", views.GearList.as_view(), name="gears_index"),
    path('accounts/signup/', views.signup, name='signup'),
]
