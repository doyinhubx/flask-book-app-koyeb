#!/bin/sh

echo "⏳ Waiting for MySQL to be ready..."
while ! nc -z db 3306; do
  sleep 1
done

echo "✅ MySQL is up - running migrations..."
flask db upgrade

echo "🚀 Starting Flask server..."
exec flask run --host=0.0.0.0
