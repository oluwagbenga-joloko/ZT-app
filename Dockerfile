FROM python:3.7

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

# install our dependencies
# we use --system flag because we don't need an extra virtualenv
COPY Pipfile Pipfile.lock /opt/services/djangoapp/src/


RUN pip install pipenv && pipenv install --dev --system


# copy entrypoint.sh
COPY ./entrypoint.sh /opt/services/djangoapp/src/entrypoint.sh


COPY . /opt/services/djangoapp/src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000


ENTRYPOINT ["/opt/services/djangoapp/src/entrypoint.sh"]

# CMD ["gunicorn", "--bind", ":8000", "mysite.wsgi:application"]