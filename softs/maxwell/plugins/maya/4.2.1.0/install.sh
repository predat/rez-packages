#!/bin/bash

BINARY_DIR=$1
PREFIX_DIR=$2
# MAJOR_VERSION=$3


if [[ $MAYA_VERSION == *"2016.5"* ]]; then

    PLUGIN_PATH=${BINARY_DIR}/maxwell_maya/src/maxwell_maya-build/maya${REZ_MAYA_MAJOR_VERSION}.${REZ_MAYA_MINOR_VERSION}

else

    PLUGIN_PATH=${BINARY_DIR}/maxwell_maya/src/maxwell_maya-build/maya${REZ_MAYA_MAJOR_VERSION}

fi


# patchel
MAXWELL_MAYA_SO=${PLUGIN_PATH}/bin/plug-ins/maxwell.so
OLD_MXCOMMON=$("${MAXWELL_ROOT}/patchelf" --print-needed "${MAXWELL_MAYA_SO}" | grep "libmxcommon.so")
NEW_MXCOMMON=${MAXWELL_ROOT}/libmxcommon.so


if [[ -f "$NEW_MXCOMMON" ]];then

    "${MAXWELL_ROOT}/patchelf" --replace-needed "$OLD_MXCOMMON" "$NEW_MXCOMMON" "$MAXWELL_MAYA_SO"

fi


# Install
for file in ${PLUGIN_PATH}/*;

do

    echo "Installing ${file}"

    cp -arf "${file}" "${PREFIX_DIR}"

done

