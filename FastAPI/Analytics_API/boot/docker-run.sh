#!/bin/bash

source /opt/venv/bin/activate
cd /code

export PYTHONPATH=/code
gunicorn main:app \
  --workers 2 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:${PORT:-8000}

