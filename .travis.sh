#!/usr/bin/env bash

#docker run -it -d -u travis -v "$(pwd)":/project quay.io/travisci/travis-python /bin/bash

BUILDID="build-1"
INSTANCE="travisci/ci-sardonyx"

docker run --name ${BUILDID} -d -it -v "$(pwd)":/ ${INSTANCE} /sbin/init
docker exec -it -u travis -w / ${BUILDID} bash -l
