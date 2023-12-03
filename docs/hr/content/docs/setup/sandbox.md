---
sidebar_position: 3
tags:
  - quickstart
---

# Sandbox

The [`pinnacledb` open-source repository](https://github.com/SuperDuperDB/pinnacledb) comes with a sandbox testing 
environment. The sandbox is implemented in `docker-compose` and includers containers for each of the services 
included in `pinnacledb`. View the details of the setup [here](https://github.com/SuperDuperDB/pinnacledb/blob/main/deploy/testenv/docker-compose.yaml).

In this environment, users can test and get a feel for a full `pinnacledb` setup, without the need to configure cloud environments or kubernetes setups. This environment may be used as inspiration for a more scalable, production-ready setup.

To build this environment first checkout the project if you haven't already:

```bash
git clone git@github.com:SuperDuperDB/pinnacledb
cd pinnacledb
```

Then build the docker image required to run the environment:

```bash
make testenv_image
```

> If you want to install additional `pip` dependencies in the image, you have to list them in `requirements.txt`.
> 
> The listed dependencies may refer to:
> 1. standalone packages (e.g `tensorflow>=2.15.0`)
> 2. dependency groups listed in `pyproject.toml` (e.g `.[demo,server]`)


Now add these configurations to your setup by running:

```bash
mkdir -p .pinnacledb
cat << Multi > .pinnacledb/config.yaml
data_backend: mongodb://pinnacle:pinnacle@mongodb:27017/test_db
cluster:
  cdc: http://cdc:8001
  compute: dask://scheduler:8786
  vector_search: in_memory://vector-search:8000
Multi
```

To start the environment run:

```bash
make testenv_init
```

This uses `docker-compose` to spin up:

- local testing `mongodb` deployment
- `jupyter` notebook environment
- `dask` scheduler
- `dask` worker
- `cdc` service
- `vector-search` service

To stop the environment run:

```bash
make testenv_shutdown
```

# Known Issues

To make sure data is saved between restarts, we connect a local data location to the `mongodb` container. 
The location is specified in the `SUPERDUPERDB_DATA_DIR` of the Makefile and is initially set to `deploy/testenv/.test_data`. 

However, since the `mongodb` container runs as 'root', the data directory will be owned by `root`, and you'll need `sudo` to delete it later.
