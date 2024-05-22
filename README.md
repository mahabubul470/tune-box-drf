
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Python](https://img.shields.io/pypi/pyversions/shurjopay-plugin)](https://badge.fury.io/py/shurjopay-plugin)
> :notebook: **Note:** This django app is built with python version 3.12-dev
#### Step 1: Install Python and Activate Virtual Environment

For managing different versions of Python, use [Pipenv](https://pipenv.pypa.io/en/latest/index.html)
Install Pipenv using pip
```
 pip install pipenv --user
```

#### Step 2: Install Project Requirements

```bash
pipenv install
```
#### Step 3: Create the .env file and configure it

```bash
cat .env.sample > .env
```
#### Step 3: Run docker compose to start the services

```bash
docker compose -f docker-compose.yml up -d --build
```


#### You can  also run the project localy using
> :notebook: **Note:** You need to setup Postgresql in your local machine
```bash
python manage.py runserver
```

#### Fetch music tracs using dezzer api 
> :notebook: **Note:** Choose artist name in the django admin management command

```bash
python manage.py fetch_deezer_tracks "beatles"
```
> :notebook: **Note:** You can also set it up on [entrypoint.sh](./entrypoint.sh) script

```bash
#!/bin/sh
python manage.py fetch_deezer_tracks "beatles"
python manage.py fetch_deezer_tracks "queen"
python manage.py fetch_deezer_tracks "eminem"
# Execute the command passed to the entrypoint script
exec "$@"

```

### Explore API's using swagger / redoc 
(https://pipenv.pypa.io/en/latest/index.html)
> :notebook: **Note:** Please authenticate using the prefix Token