FROM python:3.10.13-alpine

ENV PYTHONUNBUFFERED=1

RUN apk add g++ linux-headers libffi-dev
RUN pip install --upgrade pip
RUN python3 -m pip install --upgrade setuptools
RUN pip3 install --no-cache-dir  --force-reinstall -Iv grpcio==1.60.1
RUN pip3 install --no-cache-dir  --force-reinstall -Iv cffi==1.16.0
RUN pip3 install gunicorn

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENV PORT 8080

ENV ALLOWED_HOSTS 0.0.0.0

EXPOSE 8080

CMD exec gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 8 --timeout 0 djangoProject.wsgi:application