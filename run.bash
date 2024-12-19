#/usr/bin/bash

tmux new -d -s website 'gunicorn sse:app --worker-class gevent --bind 127.0.0.1:8001'
tmux new -d -s discbot 'uvicorn bot:app --reload --port 8080 --host 0.0.0.0'
