#!/usr/bin/env bash
# Exit on error
set -o errexit

# 1. Install dependencies
pip install -r requirements.txt

# 2. Collect Static Files (CSS/JS)
# This gathers all your assets into a single folder for WhiteNoise to serve.
python manage.py collectstatic --no-input

# 3. Database Migrations
# This updates your PostgreSQL schema to match your models.
python manage.py migrate