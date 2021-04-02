FROM python:3.8-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR /mysite
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY mysite/ .
COPY oxigeno-cc-4d2523dd547c.json .