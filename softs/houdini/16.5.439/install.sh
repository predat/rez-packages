#!/bin/bash
BINARY_DIR=$1
PREFIX_DIR=$2
HOUDINI_VERSION=$3
HOUDINI_ROOT="${BINARY_DIR}/houdini/src/houdini"
PYTHON_VERSIONS="2.7"

mkdir -p ${PREFIX_DIR}/houdini
echo "Installing houdini files."
tar -zxf "${BINARY_DIR}/houdini/src/houdini/houdini.tar.gz" -C "${PREFIX_DIR}/houdini"

mkdir "${PREFIX_DIR}/houdini/python"
cd "${PREFIX_DIR}/houdini/python"
echo "Installing python library dependencies."
tar -zxf "${BINARY_DIR}/houdini/src/houdini/pythonlibdeps.tar.gz"

echo "Installing Python ${PYTHON_VERSIONS} distribution."
for py_ver in ${PYTHON_VERSIONS}; do
    tar -zxf "${BINARY_DIR}/houdini/src/houdini/python${py_ver}.tar.gz"
done
