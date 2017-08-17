#!/usr/bin/env bash

BINARY_DIR=$1
PREFIX_DIR=$2
MAXWELL_MAJOR_VERSION=$3
MAXWELL_INSTALL_ROOT="${BINARY_DIR}/maxwell/src/maxwell-build"

echo "BINARY: ${BINARY_DIR}"
echo "PREFIX: ${PREFIX_DIR}"

cp -ra ${BINARY_DIR}/maxwell/src/maxwell/maya2017 ${PREFIX_DIR}/maxwell

patchelf --replace-needed \
    /usr/local/maxwell-render-4.1/libmxcommon.so \
    ${REZ_MAXWELL_ROOT}/maxwell/libmxcommon.so \
    ${PREFIX_DIR}/maxwell/bin/plug-ins/maxwell.so
