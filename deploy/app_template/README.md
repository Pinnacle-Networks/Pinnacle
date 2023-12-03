# App-template for serving `pinnacledb`

## Running with docker

To run this sample app, build the image with:

```bash
make testenv_image
```

And run the app with:

```bash
docker run -it -p 8000:8000 -v /Users/dodo/SuperDuperDB/pinnacledb:/home/pinnacle/pinnacledb pinnacledb/sandbox uvicorn deploy.app_template.app:app --host <host>
```