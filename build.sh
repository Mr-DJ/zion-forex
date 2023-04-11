#!/bin/bash

echo "Building projecc.."
python3.9 -m pip install -r requirements.txt

echo "Migrations.."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect static.."
python3.9 manage.py collectstatic --noinput --clear