#!/bin/bash

# Run database migrations
python manage.py migrate

# Collect static files for production
python manage.py collectstatic --no-input

# Start the Gunicorn server, binding to the port set by the platform
gunicorn Sha_Web.wsgi --bind 0.0.0.0:$PORT