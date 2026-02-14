#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Run Django commands from the www directory where manage.py is located
python ./www/manage.py collectstatic --no-input
python ./www/manage.py migrate