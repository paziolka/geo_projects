# Geo projects

This is a simple CRUD projects application built using FastAPI.

## About

“Project” in our terminology is basically a plot of land, that we will be analyzing by utilizing the satellite imagery captured in selected date range.

## How to setup

### Using Docker

##### Prerequisites

Before getting started, make sure you have Docker installed on your system. You can download and install Docker from [here](https://www.docker.com/get-started).

##### Run & test

To start the FastAPI application using Docker Compose, navigate to the directory containing the docker-compose.yml file and run the following command:

```bash
docker-compose up -d
```

This will build the Docker image (if not already built) and start the FastAPI application in detached mode.

In order to run pytest using Docker Compose, you would execute the following command:

```bash
docker-compose run pytest
```

