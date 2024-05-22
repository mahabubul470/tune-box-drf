from rest_framework import serializers
from .models import Track, Playlist, PlaylistTrack

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'

class PlaylistTrackSerializer(serializers.ModelSerializer):
    track = TrackSerializer()

    class Meta:
        model = PlaylistTrack
        fields = ['track']

class PlaylistSerializer(serializers.ModelSerializer):
    tracks = PlaylistTrackSerializer(source='playlisttrack_set', many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = ['id', 'name', 'user', 'is_public', 'tracks']
        read_only_fields = ['user']

class TokenDestroySerializer(serializers.Serializer):
    pass
