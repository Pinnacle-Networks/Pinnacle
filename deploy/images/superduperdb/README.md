# SuperDuperDB Image

This image wraps the SuperDuperDB framework into a [Jupyter Notebook.](https://github.com/jupyterhub/zero-to-jupyterhub-k8s/blob/main/images/singleuser-sample/Dockerfile) 

Additionally, the image is shipped with a variety of examples from the SuperDuperDB [use-cases.](https://github.com/SuperDuperDB/pinnacledb/tree/main//docs/content/use_cases/items)


To build the image: 

```shell
docker build -t pinnacledb/pinnacledb:latest   ./  --progress=plain
```


To run the image:

```shell
docker run -p 8888:8888 pinnacledb/pinnacledb:latest
``` 