FROM python:3.8-alpine3.11
COPY ./pybumpversion.py /app/pybumpversion.py
ENTRYPOINT ["/app/pybumpversion.py"]
