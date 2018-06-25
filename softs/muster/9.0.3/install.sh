#!/bin/bash

BINARY_DIR=$1
PREFIX_DIR=$2
# MAJOR_VERSION=$3

echo "Installing Muster files."
for file in ${BINARY_DIR}/muster/src/muster/*
do
    echo "Installing: ${file}"
    cp -arf "${file}" "$PREFIX_DIR"
done

cd $PREFIX_DIR
chmod 755 plugins scripts templates htdocs extra python python/Lib
