FROM node:13.12.0-alpine as build

WORKDIR /app/frontend
COPY ./frontend/package.json ./
COPY ./frontend/package-lock.json ./

COPY ./frontend/ ./
EXPOSE 8000

CMD ["/bin/sh", "-c" , "npm install && PORT=8000 npm start" ]
