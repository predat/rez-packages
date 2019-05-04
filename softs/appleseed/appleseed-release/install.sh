#!/bin/bash

NAME=${REZ_BUILD_PROJECT_NAME}
VERSION=${REZ_BUILD_PROJECT_VERSION}
ARCHIVE=${NAME}-${VERSION}-0-g5cff7b96b-linux64-gcc48
EXT='zip'
BASE_URL="https://github.com/appleseedhq/appleseed/releases/download/2.0.0-beta/appleseed-2.0.0-beta-0-g5cff7b96b-linux64-gcc48.zip"
MD5SUM="092da084b0c6f0b4871e478ae308aa8c"

cd ${REZ_BUILD_PATH}

echo -n "* Downloading archive: $ARCHIVE.${EXT} ..."
if [[ -f $ARCHIVE.$EXT ]]; then
    echo " skip: archive already downloaded."
else
    cp /home/predat/Downloads/appleseed-2.0.0-beta-0-g5cff7b96b-linux64-gcc48.zip .
    # wget "${BASE_URL}"
    echo
fi


echo -n "* Verifying checksum..."
if [[ $MD5SUM != $(md5sum "${ARCHIVE}.${EXT}"|awk '{print $1}') ]]; then
    echo " bad checksum. Exit."
    exit 1;
else
    echo " look's good."
fi


echo -n "* Decompressing archive..."
if [[ ! -d ${ARCHIVE} ]]; then
    unzip -q ${ARCHIVE}.${EXT}
    echo " ok"
else
    echo " skip: folder already exists."
fi


echo "* Copy files to install location (${REZ_BUILD_INSTALL_PATH})"
cp -ar appleseed/* ${REZ_BUILD_INSTALL_PATH}
