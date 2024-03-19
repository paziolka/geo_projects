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
~~In order to run pytest using Docker Compose, you would execute the following command:~~
Tests are not working yet, due to db setup, last SHA they've worked: 

```bash
git checkout 73ff52130b47424ed0ad158fd178af65e8e23468
docker-compose run pytest
git checkout main
```

### Problems to solve
* multiple requests/duplicated results (would be name validation enough?)
* setting up test database (pytest-postgresql?)
* linter (black?) I need sth
* migrations in case of adding new db fields (alembic?)
* daterange - after spending too much time on [this issue](https://github.com/tiangolo/sqlmodel/issues/235) I decided that implementing dateranges by myslef at this stage would end up in too much of a code I don't fully understand, so I decided to go with start_date and end_date with validations.
