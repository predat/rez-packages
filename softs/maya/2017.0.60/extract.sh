#!/usr/bin/env bash
BINARY_DIR=$1
SOURCE_DIR=$2
MAYA_MAJOR_VERSION=$3
MAYA_ROOT="${BINARY_DIR}/maya/src/maya-build/usr/autodesk/maya${MAYA_MAJOR_VERSION}"
if [ "$MAYA_MAJOR_VERSION" == "2015" ];
then
  MAYA_ROOT=${MAYA_ROOT}-x64
fi
ADLM_OPT_ROOT="${BINARY_DIR}/maya/src/maya-build/opt/Autodesk/Adlm"

echo "Extracting Maya rpm's."
if [ -d "$MAYA_ROOT" ]; then
  echo "rpm already extracted skipping."
else
  for rpm_file in `ls ${BINARY_DIR}/maya/src/maya/Maya*.rpm`;
  do
    rpm2cpio ${rpm_file} | cpio -idm -W none;
  done
fi
echo ""

echo "Extracting Adlm rpm's."
if [ -d "$ADLM_OPT_ROOT" ]; then
  echo "rpm already extracted skipping."
else
  for rpm_file in `ls ${BINARY_DIR}/maya/src/maya/adlmapps*.rpm`;
  do
    rpm2cpio ${rpm_file} | cpio -idm -W none;
  done
fi
echo ""

