# ZT App

A simple application built built [django](https://www.djangoproject.com/) and [SQLite](https://www.sqlite.org/index.html) as data store that displays temperature measurement.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
  

### Prerequisites

Download [Docker Desktop](https://www.docker.com/products/docker-desktop) for Mac or Windows. [Docker Compose](https://docs.docker.com/compose) will be automatically installed. On Linux, make sure you have the latest version of [Compose](https://docs.docker.com/compose/install/).

### Installing

A step by step series of examples that tell you how to get a development env running


- clone the repository


```bash

git clone git@github.com:oluwagbenga-joloko/ZT-app.git && cd ZT-app
```

> Data is added to the Database automatically through a `seed_temp` management command in Dockerfile. 

``` bash

docker-compose up --build

```

- The app should now be available from your browser at `http://127.0.0.1:8000`



### Docker Hub
- Application is also available on docker Hub via the command below

``` bash
docker pull gbengajoloko/zt_app:latest
```

- run the application

```bash
sudo docker run -it -p 8000:8000 gbengajoloko/zt_app:latest
```
- The app should now be available from your browser at `http://127.0.0.1:8000`
