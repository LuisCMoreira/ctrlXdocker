#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

TARGET_ARCH=$1
echo TARGET_ARCH: ${TARGET_ARCH}
IMAGE_NAME1="ctrlx-datalayer-robotui"
IMAGE_TAG="latest"
DOCKER_CLI=$(which docker)
echo --- add image env variables
echo IMAGE_NAME=${IMAGE_NAME} >> ../docker-compose/docker-compose.env
echo IMAGE_TAG=${IMAGE_TAG} >> ../docker-compose/docker-compose.env
echo --- create ctrlx-datalayer-robotui docker image with platform ${TARGET_ARCH}
${DOCKER_CLI} buildx build -f ../docker-compose/Dockerfile_robot --platform linux/${TARGET_ARCH} -t ${IMAGE_NAME}:${IMAGE_TAG} --output "type=docker,name=${IMAGE_NAME}:${IMAGE_TAG}" --build-context project=../ctrlx-datalayer-robotui  .
${DOCKER_CLI} save ${IMAGE_NAME}:${IMAGE_TAG} | gzip > ../docker-compose/image.tar.gz
${DOCKER_CLI} rmi ${IMAGE_NAME}:${IMAGE_TAG}
