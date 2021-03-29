#!/usr/bin/env bash

. ./app-venv/bin/activate
export FLASK_APP=app.py
export FLASK_ENV=development
export PYTHONUNBUFFERED=True

flask run -h 127.0.0.1