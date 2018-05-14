#!/bin/bash

BINARY_DIR=$1
PREFIX_DIR=$2
INSTALL_ROOT=${BINARY_DIR}/appleseed/src/appleseed


for f in ${INSTALL_ROOT}/*
do
    echo "Installing: ${f}"
    cp -rf "${f}" "${PREFIX_DIR}"
done

# Remove libexpat.so.1 from appleseed lib folder
# because it require GLIBC_2.25
rm "${PREFIX_DIR}"/lib/libexpat.so.1
