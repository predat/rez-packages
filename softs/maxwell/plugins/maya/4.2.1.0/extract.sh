#!/bin/bash

BINARY_DIR=$1
# PREFIX_DIR=$2
# MAJOR_VERSION=$3

for pkg in ${BINARY_DIR}/maxwell_maya/src/maxwell_maya/${REZ_BUILD_PROJECT_NAME//_/-}${REZ_MAYA_MAJOR_VERSION}*.tar.gz;
do
    echo "Extracting plugin for Maya ${REZ_MAYA_MAJOR_VERSION}"
    tar -zxvf "${pkg}"
done
