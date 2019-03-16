# Docker Exercise # 2
There Are 3 directories, one for each exercise.

## Aws Cli
This directory contains a Dockerfile using Alpine Base Image and it installs AWS Cli on the container.

To create and run the container cd inside the directorie and run the following commands:
```bash
docker build -t awscli .
docker run awscli
```

## Docker
This directory contains a Dokcerfile using Alpine Base Image and it installs Docker and Docker-compose inside the container.

To create and run the container cd inside the directorie and run the following commands:
```bash
docker build -t awscli .
docker run awscli
```

## Compose
This directory contains a docker-compose file and 3 sub-directories one for each service installed.

![Diagram](https://github.com/DeboraArzu/DockerExercise/blob/master/Docker-Compose.jpg "Diagram")

To create and run the container cd inside the directorie and run the following commands:
```bash
docker-compose up
```


