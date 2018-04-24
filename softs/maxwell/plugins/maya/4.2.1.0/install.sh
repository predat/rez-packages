#!/bin/bash

BINARY_DIR=$1
PREFIX_DIR=$2
# MAJOR_VERSION=$3


# patchel
MAXWELL_MAYA_SO=${BINARY_DIR}/maxwell_maya/src/maxwell_maya-build/maya${REZ_MAYA_MAJOR_VERSION}/bin/plug-ins/maxwell.so
OLD_MXCOMMON=$("${MAXWELL_ROOT}/patchelf" --print-needed "${MAXWELL_MAYA_SO}" | grep "libmxcommon.so")
NEW_MXCOMMON=${MAXWELL_ROOT}/libmxcommon.so
if [[ -f "$NEW_MXCOMMON" ]];then
    "${MAXWELL_ROOT}/patchelf" --replace-needed "$OLD_MXCOMMON" "$NEW_MXCOMMON" "$MAXWELL_MAYA_SO"
fi


# Install
for file in ${BINARY_DIR}/maxwell_maya/src/maxwell_maya-build/maya${REZ_MAYA_MAJOR_VERSION}/*;
do
    echo "Installing ${file}"
    cp -arf "${file}" "${PREFIX_DIR}"
done

