#!/bin/sh

# Run migrations and collect static files
python manage.py migrate
python manage.py collectstatic --no-input --clear
python manage.py fetch_deezer_tracks "beatles"
python manage.py fetch_deezer_tracks "queen"
python manage.py fetch_deezer_tracks "eminem"


# Execute the command passed to the entrypoint script
exec "$@"
