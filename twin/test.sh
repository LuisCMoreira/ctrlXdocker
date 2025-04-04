#!/bin/bash
./scripts/docker_clean.sh
docker buildx build -f ./docker-compose/Dockerfile_robot --platform linux/amd64 -t "robotui:latest" --output "type=docker,name=robotui:latest" --build-context project=./ctrlx-datalayer-robotui  .
docker buildx build -f ./docker-compose/Dockerfile_ui --platform linux/amd64 -t "ui:latest" --output "type=docker,name=ui:latest" --build-context project=./ctrlx-datalayer-mqtt-ui  .