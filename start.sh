#!/bin/sh

echo "⏳ Waiting for postgres..."

# Wait until Postgres is ready
while ! nc -z db 5432; do
  sleep 1
done

echo "✅ Postgres is up - starting FastAPI..."

# Run the FastAPI app using Uvicorn
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
