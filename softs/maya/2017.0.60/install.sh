#!/usr/bin/env bash
BINARY_DIR=$1
PREFIX_DIR=$2
MAYA_MAJOR_VERSION=$3
MAYA_ROOT="${BINARY_DIR}/maya/src/maya-build/usr/autodesk/maya${MAYA_MAJOR_VERSION}"
if [ "$MAYA_MAJOR_VERSION" == "2015" ];
then
  MAYA_ROOT=${MAYA_ROOT}-x64
fi

ADLM_OPT_ROOT="${BINARY_DIR}/maya/src/maya-build/opt/Autodesk/Adlm"
ADLM_VAR_ROOT="${BINARY_DIR}/maya/src/maya-build/var/opt/Autodesk/Adlm"
echo "BINARY: ${BINARY_DIR}"
echo "MAYA_ROOT: ${MAYA_ROOT}"
echo "PREFIX: ${PREFIX_DIR}"

mkdir -p ${PREFIX_DIR}/maya
echo "Installing maya root folder."
for directory in $(ls ${MAYA_ROOT});
do
  echo "Installing: ${MAYA_ROOT}/${directory}"
  cp -rf ${MAYA_ROOT}/${directory} ${PREFIX_DIR}/maya/
done
echo ""

mkdir -p ${PREFIX_DIR}/Adlm/{opt,var}
echo "Installing adlm opt folder."
for directory in $(ls ${ADLM_OPT_ROOT});
do
  echo "Installing: ${ADLM_OPT_ROOT}/${directory}"
  cp -rf ${ADLM_OPT_ROOT}/${directory} ${PREFIX_DIR}/Adlm/opt/
done
echo ""

echo "Installing adlm var folder."
for directory in $(ls ${ADLM_VAR_ROOT});
do
  echo "Installing: ${ADLM_VAR_ROOT}/${directory}"
  cp -rf ${ADLM_VAR_ROOT}/${directory} ${PREFIX_DIR}/Adlm/var/
done
