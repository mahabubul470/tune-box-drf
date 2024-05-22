from rest_framework import generics, permissions
from django.db.models import Q
from .models import Track, Playlist
from .serializers import TrackSerializer, PlaylistSerializer, TokenDestroySerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter
from djoser.views import TokenDestroyView

@extend_schema(
    responses={204: None}
)
class CustomTokenDestroyView(TokenDestroyView):
    serializer_class = TokenDestroySerializer


@extend_schema(
    responses=TrackSerializer,
    description="List and create music tracks."
)
class TrackListCreateView(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

@extend_schema(
    responses=PlaylistSerializer,
    description="List and create playlists. Authenticated users can create playlists."
)
class PlaylistListCreateView(generics.ListCreateAPIView):
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Playlist.objects.filter(user=self.request.user) | Playlist.objects.filter(is_public=True)
        return Playlist.objects.filter(is_public=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@extend_schema(
    responses=PlaylistSerializer,
    description="Retrieve, update, or delete a specific playlist."
)
class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

@extend_schema(
    responses=PlaylistSerializer,
    description="List all playlists of the logged-in user."
)
class UserPlaylistsView(generics.ListAPIView):
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Playlist.objects.filter(user=user)
        return Playlist.objects.none()

@extend_schema(
    responses=PlaylistSerializer,
    description="List all public playlists."
)
class PublicPlaylistsView(generics.ListAPIView):
    queryset = Playlist.objects.filter(is_public=True)
    serializer_class = PlaylistSerializer

@extend_schema(
    parameters=[
        OpenApiParameter(name='q', description='Search query', required=True, type=str)
    ],
    responses=PlaylistSerializer,
    description="Search playlists by name."
)
class PlaylistSearchView(generics.ListAPIView):
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query:
            if self.request.user.is_authenticated:
                return Playlist.objects.filter(
                    Q(name__icontains=query, user=self.request.user) | Q(name__icontains=query, is_public=True)
                )
            else:
                return Playlist.objects.filter(name__icontains=query, is_public=True)
        return Playlist.objects.none()






