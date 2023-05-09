FROM python:3.10

WORKDIR /test-app

COPY . .

RUN pip install pylint
