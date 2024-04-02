---
sidebar_position: 1
---

# Developer vs. production mode

Please refer to the [architecture](../fundamentals/architecture.md) page for a detailed description of the `pinnacledb` architecture.

There are several important services in a `pinnacledb` setup which may be run in-process, or in their 
own micro-services and containers:

- `jupyter` notebook/ client
- change-data-capture (CDC) service
- compute
  - scheduler
  - workers
- vector-searcher service

## Development mode

With the default settings of `pinnacledb`, all of these items run in a single process.
This is great for:

- Debugging
- Prototyping
- Experimentation
- Exploration
- Querying `pinnacledb`

## Production

There are several gradations of a more productionized deployment.
In the most distributed case we have:

- A `jupyter` environment running in its own process
- A [distributed **Dask** cluster](non_blocking_dask_jobs.md), with scheduler and workers configured to work with `pinnacledb`
- A [**change-data-capture** service](change_data_capture.md)
- A [**vector-search** service](vector_comparison_service.md), which finds similar vectors, given an input vector

In the remainder of this section we describe the use of each of these services