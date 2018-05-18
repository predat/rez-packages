#!/bin/bash

BINARY_DIR=$1
PREFIX_DIR=$2
MAJOR_VERSION=$3

echo "       $BINARY_DIR $PREFIX_DIR $MAJOR_VERSION"

echo "Installing RV files."
for file in ${BINARY_DIR}/rv/src/rv/*
do
    echo "Installing: ${file}"
    cp -arf "${file}" "$PREFIX_DIR"
done

