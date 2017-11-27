# Dockerfile

FROM python:3
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN mkdir Features
RUN mkdir Output

RUN pip install -r requirements.txt

RUN chmod +x /code/start.sh

CMD ["/code/start.sh"]
