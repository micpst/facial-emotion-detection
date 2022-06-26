# Facial Emotion Detection

## Quick start
Build the development container image:
```
$ docker build . \
  -f ./docker/Dockerfile-dev \
  -t web-app
```

Start an app container:
```
$ docker run \
  -dp 5000:5000 \
  --env-file ./env/.env.dev \
  -v "$(pwd)"/:/opt/code \
  web-app
```

## License
All my code is MIT licensed. Libraries follow their respective licenses.