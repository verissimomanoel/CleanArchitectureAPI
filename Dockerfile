FROM python:3.10-buster

ENV PYTHONUNBUFFERED=1
ENV HOST=0.0.0.0
ENV PORT=8000

WORKDIR /code
COPY . /code/

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

RUN ls
RUN ls app

CMD uvicorn app.infrastructure.application:app --host ${HOST} --port ${PORT}
