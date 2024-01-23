FROM python:alpine3.17

COPY main.py /app.py

USER 1000

ENTRYPOINT [ "python3", "/app.py" ]
