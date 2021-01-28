FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /mysite
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt update -y && apt install netcat -y
ENV DB_HOST=db
ENV DB_PORT=5432

COPY mysite/ .
COPY .env .
COPY entrypoint.sh .
RUN chmod +x /mysite/entrypoint.sh
