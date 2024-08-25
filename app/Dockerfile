FROM python:3.8.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD admin

RUN mkdir /app
COPY . /mysite
WORKDIR /mysite

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --noinput && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py createsuperuser --user admin --email javad@gmail.com --noinput; \
    gunicorn -b 0.0.0.0:8000 config.wsgi --timeout 500