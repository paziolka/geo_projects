# Geo projects

This is a simple CRUD projects application built using FastAPI.

## About

“Project” in our terminology is basically a plot of land, that we will be analyzing by utilizing the satellite imagery captured in selected date range.

## How to setup

### Using Docker

##### Prerequisites

Before getting started, make sure you have Docker installed on your system. You can download and install Docker from [here](https://www.docker.com/get-started).

##### Run

To start the FastAPI application using Docker Compose, navigate to the directory containing the docker-compose.yml file and run the following command:

```bash
docker-compose build
docker-compose up web -d
```

This will build the Docker image (if not already built) and start the FastAPI application in detached mode.

In case of problems with db initialization locally, ensure:

```bash
docker-compose exec db psql --username=geo_projects --dbname=geo_projects
```

Check the app API under: `http://127.0.0.1:8008/docs`
##### Test
In order to run pytest using Docker Compose, you would execute the following command:

```bash
docker-compose run pytest
```

