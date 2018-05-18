#!/bin/bash

BINARY_DIR=$1
PREFIX_DIR=$2
INSTALL_ROOT=${BINARY_DIR}/blenderseed/src/blenderseed


mkdir -p "${PREFIX_DIR}/addons/blenderseed"

for f in ${INSTALL_ROOT}/*
do
    echo "Installing: ${f}"
    cp -rf "${f}" "${PREFIX_DIR}/addons/blenderseed"
done

