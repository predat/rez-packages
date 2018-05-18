#!/usr/bin/env bash
BINARY_DIR=$1
SOURCE_DIR=$2
MAXWELL_MAJOR_VERSION=$3
#MAXWELL_ROOT="${BINARY_DIR}/maxwell/src/maxwell-build/${MAYA_MAJOR_VERSION}"

echo "BINARY:  " + $BINARY_DIR
echo "SOURCE:  " + $SOURCE_DIR
echo "version: " + $REZ_BUILD_PROJECT_VERSION

echo "Extracting Maxwell zip file."
#echo "-------- unzip in " + $PWD
unzip -q $SOURCE_DIR/archives/maxwell-maya-linux-${REZ_BUILD_PROJECT_VERSION}.zip

cp ${SOURCE_DIR}/config/installer_response.txt ${BINARY_DIR}/

#echo $(env)
