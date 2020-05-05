FROM python:3.7-alpine

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

# install our dependencies
# we use --system flag because we don't need an extra virtualenv
COPY Pipfile Pipfile.lock /opt/services/djangoapp/src/


RUN pip install pipenv && pipenv install --dev --system


COPY . /opt/services/djangoapp/src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py seed_temp && python manage.py runserver 0.0.0.0:8000"]