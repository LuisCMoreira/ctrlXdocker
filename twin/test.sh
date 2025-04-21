#!/bin/bash
./scripts/docker_clean.sh
docker buildx build -f ./docker-compose/Dockerfile_robot --platform linux/amd64 -t "robotui:latest" --output "type=docker,name=robotui:latest" --build-context project=./ctrlx-datalayer-robotui  .