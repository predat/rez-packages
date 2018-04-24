#!/bin/bash

BINARY_DIR=$1
SOURCE_DIR=$2
VERSION=$3

echo "------------- BINARY_DIR=$BINARY_DIR"
echo "------------- SOURCE_DIR=$SOURCE_DIR"
echo "------------- VERSION=${VERSION}"

echo "Extracting Nuke files."
# unzip ${BINARY_DIR}/nuke/src/nuke/

ARCH=$(echo "$REZ_ARCH_VERSION" | cut -f1 -d'_')
BITS=$(echo "$REZ_ARCH_VERSION" | cut -f2 -d'_')
APP_NAME=$(echo "$REZ_BUILD_PROJECT_NAME" | sed 's/[^ ]\+/\L\u&/g')

# Nuke11.1v3-linux-x86-release-64-installer
#unzip "${BINARY_DIR}/nuke/src/nuke/${APP_NAME}${NUKE_VERSION}-${REZ_PLATFORM_VERSION}-${ARCH}-release-${BITS}-installer" -d ${BINARY_DIR}/nuke/src/nuke-build/
unzip "${BINARY_DIR}/nuke/src/nuke/${APP_NAME}${VERSION}-${REZ_PLATFORM_VERSION}-${ARCH}-release-${BITS}-installer" -d ${BINARY_DIR}/nuke/src/nuke-build/
