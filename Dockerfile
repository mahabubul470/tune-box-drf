FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update \
    && apt-get install -y netcat-openbsd \
    && apt-get clean

# Set working directory
WORKDIR /code

# Install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /code/

# Install dependencies
RUN pipenv install --system --deploy

# Copy project files
COPY . /code/

# Add entrypoint.sh to the container
COPY entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh

# Command to run the entrypoint script
ENTRYPOINT ["/code/entrypoint.sh"]
