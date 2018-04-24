#!/bin/bash

BINARY_DIR=$1
PREFIX_DIR=$2
#NUKE_VERSION=$3

NUKE_ROOT=${BINARY_DIR}/nuke/src/nuke-build

mkdir -p "${PREFIX_DIR}/nuke"
echo "Installing nuke root folder."
for directory in $(ls ${NUKE_ROOT});
do
    echo "Installing: ${NUKE_ROOT}/${directory}"
    cp -rf "${NUKE_ROOT}/${directory}" "${PREFIX_DIR}/nuke"
done
echo ""
