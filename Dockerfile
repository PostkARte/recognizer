FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
Add ./requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt
