#!/bin/bash

exec gunicorn PostkARteRecognizer.wsgi --bind 0.0.0.0:8000 --workers 3
