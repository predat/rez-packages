#!/bin/bash

BINARY_DIR=$1
PREFIX_DIR=$2
BLENDER_INSTALL_ROOT=${BINARY_DIR}/blender/src/blender


for f in ${BLENDER_INSTALL_ROOT}/*
do
    echo "Installing: ${f}"
    cp -rf "${f}" "${PREFIX_DIR}"
done
