#!/bin/bash

BINARY_DIR=$1
PREFIX_DIR=$2
MAJOR_VERSION=$3

echo "       $BINARY_DIR $PREFIX_DIR $MAJOR_VERSION $4"

echo "Installing ${4} files."
for file in ${BINARY_DIR}/maxwell/src/${4}/*
do
     echo "Installing: ${file}"
     cp -arf "${file}" "$PREFIX_DIR"
 done
