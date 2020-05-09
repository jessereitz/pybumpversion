FROM python:3.8-alpine3.11
WORKDIR /app
COPY ./bumpversion.py /app/bumpversion.py

ENTRYPOINT ["/app/bumpversion.py"]
