from django.urls import path
from .views import (
    TrackListCreateView,
    PlaylistListCreateView,
    PlaylistDetailView,
    UserPlaylistsView,
    PublicPlaylistsView,
    PlaylistSearchView,
)

urlpatterns = [
    path('tracks/', TrackListCreateView.as_view(), name='track-list-create'),
    path('playlists/', PlaylistListCreateView.as_view(), name='playlist-list-create'),
    path('playlists/<int:pk>/', PlaylistDetailView.as_view(), name='playlist-detail'),
    path('playlists/user/', UserPlaylistsView.as_view(), name='user-playlists'),
    path('playlists/public/', PublicPlaylistsView.as_view(), name='public-playlists'),
    path('playlists/search/', PlaylistSearchView.as_view(), name='playlist-search'),
]
