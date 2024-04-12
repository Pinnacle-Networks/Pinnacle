# Configuring models to ingest features from other models

There are two ways to connect models in `pinnacledb`:

- via interdependent `Listeners`
- via the `Graph` component

In both cases, the first step is define the computation graph using 
a simple formalism.

## Building a computation graph

`pinnacledb` supports directly acyclic graphs:

- ...
- ...
