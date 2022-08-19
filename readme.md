# Info
A toy repo to demonstrate how to:

- create a local airflow instance in docker
- show how to extend the Dockerfile by
    - installing command line tools `vim` and `ffmpeg`
    - installing pip packages `pandas` and `telethon`
- adds a simple dag to print package versions


# Usage
Mostly follow the instructions shown [here](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html).

Note: creating `.env` file and assigning a AIRFLOW_UID is a good idea. 

Before you run airflow container locally for the first time, make sure you run `docker-compose up airflow-init`. 

Then, each time you make a chance to the Dockerfile, run 
`docker compose build`.

To stand up the service, run
`docker compose up` 
