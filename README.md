# Facial Emotion Detection

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/micpst/facial-emotion-detection/blob/master/notebook/facial-emotion-detection.ipynb)

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