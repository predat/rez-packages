#!/bin/bash

NAME=${REZ_BUILD_PROJECT_NAME}
VERSION=${REZ_BUILD_PROJECT_VERSION}
ARCHIVE=${NAME}-${VERSION}-linux
EXT='tar.gz'
BASE_URL="https://github.com/GafferHQ/gaffer/releases/download"
MD5SUM="089501713556eaa98cf7f3f432042931"

cd ${REZ_BUILD_PATH}

echo -n "* Downloading archive: $ARCHIVE.${EXT} ..."
if [[ -f $ARCHIVE.$EXT ]]; then
    echo " skip: archive already downloaded."
else
    wget -q "${BASE_URL}/${VERSION}/${ARCHIVE}.${EXT}"
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
    tar -xf ${ARCHIVE}.${EXT}
    echo " ok"
else
    echo " skip: folder already exists."
fi


echo "* Copy files to install location (${REZ_BUILD_INSTALL_PATH})"
cp -ar "${ARCHIVE}/"* ${REZ_BUILD_INSTALL_PATH}
