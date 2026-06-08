#!/bin/bash
set -e

echo "Waiting for PostgreSQL to be ready..."
until /venv/bin/python -c "
import os, psycopg2
psycopg2.connect(
    dbname=os.environ['POSTGRES_DB'],
    user=os.environ['POSTGRES_USER'],
    password=os.environ['POSTGRES_PASSWORD'],
    host=os.environ.get('POSTGRES_HOST', 'db'),
    port=os.environ.get('POSTGRES_PORT', '5432'),
)
" 2>/dev/null; do
  echo "PostgreSQL not ready yet, retrying in 2s..."
  sleep 2
done

echo "PostgreSQL is ready."

echo "Running migrations..."
/venv/bin/python manage.py migrate --no-input

echo "Collecting static files..."
/venv/bin/python manage.py collectstatic --no-input

echo "Starting uWSGI..."
exec /venv/bin/uwsgi --ini /code/uwsgi.ini
