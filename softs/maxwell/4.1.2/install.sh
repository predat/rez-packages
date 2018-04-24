#!/usr/bin/env bash

BINARY_DIR=$1
PREFIX_DIR=$2
MAXWELL_MAJOR_VERSION=$3
MAXWELL_INSTALL_ROOT="${BINARY_DIR}/maxwell/src/maxwell-build"

mkdir -p ${PREFIX_DIR}/maxwell

echo "BINARY: ${BINARY_DIR}"
echo "PREFIX: ${PREFIX_DIR}"

mkdir -p ${PREFIX_DIR}/maxwell

echo "Installing Maxwell render (prefix=${PREFIX_DIR}/maxwell)."
$MAXWELL_INSTALL_ROOT/maxwell_render_4.1.1.1_linux64 \
  --mode silent \
  --response-file installer_response.txt \
  --prefix "${PREFIX_DIR}/maxwell"
