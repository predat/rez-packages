#!/bin/bash

ROOT=$1
DESTINATION=$2

lib_files=$(ls ${ROOT}/build/*_release/libtbb*)
echo "Create target directory: ${DESTINATION}/lib"
mkdir -p ${DESTINATION}/lib
echo "Copy libraries"
cp -f ${lib_files} ${DESTINATION}/lib
echo "Create target directory: ${DESTINATION}/include"
mkdir -p ${DESTINATION}/include
echo "Copy include directories"
cp -rf ${ROOT}/include/serial ${DESTINATION}/include
cp -rf ${ROOT}/include/tbb ${DESTINATION}/include