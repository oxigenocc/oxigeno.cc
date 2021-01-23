FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /mysite
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY mysite/ .

