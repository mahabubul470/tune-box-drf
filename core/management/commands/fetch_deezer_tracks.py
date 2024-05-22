import requests
from django.core.management.base import BaseCommand
from core.models import Track

class Command(BaseCommand):
    help = 'Fetch tracks from Deezer API and save them to the database'

    def add_arguments(self, parser):
        parser.add_argument('query', type=str, help='Search query for fetching tracks from Deezer')

    def handle(self, *args, **options):
        query = options['query']
        response = requests.get(f'https://api.deezer.com/search?q={query}')
        
        if response.status_code == 200:
            data = response.json()
            tracks = data.get('data', [])
            for track_data in tracks:
                title = track_data.get('title')
                artist = track_data.get('artist', {}).get('name')
                url = track_data.get('preview')
                
                if title and artist and url:
                    track, created = Track.objects.get_or_create(
                        title=title,
                        artist=artist,
                        defaults={'url': url}
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Successfully added track: {title} by {artist}'))
                    else:
                        self.stdout.write(self.style.WARNING(f'Track already exists: {title} by {artist}'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to fetch tracks. Status code: {response.status_code}'))
