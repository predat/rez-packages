#!/bin/bash

BINARY_DIR=$1
PREFIX_DIR=$2

mkdir "${PREFIX_DIR}/plug-ins"
cp "${BINARY_DIR}/appleseed_maya/src/appleseed_maya-build/src/appleseedmaya/appleseedMaya.so" "${PREFIX_DIR}/plug-ins"

cp -ar "${BINARY_DIR}/appleseed_maya/src/appleseed_maya/icons" "${PREFIX_DIR}/"
cp -ar "${BINARY_DIR}/appleseed_maya/src/appleseed_maya/presets" "${PREFIX_DIR}/"
cp -ar "${BINARY_DIR}/appleseed_maya/src/appleseed_maya/renderDesc" "${PREFIX_DIR}/"
cp -ar "${BINARY_DIR}/appleseed_maya/src/appleseed_maya/scripts" "${PREFIX_DIR}/"
cp -ar "${BINARY_DIR}/appleseed_maya/src/appleseed_maya/prefs" "${PREFIX_DIR}/"


cat<<EOF > "${PREFIX_DIR}/appleseed-maya.mod"
+ MAYAVERSION:${MAYA_VERSION} PLATFORM:linux appleseed-maya 1.1.0-beta .
plug-ins: plug-ins/
PATH +:= ${REZ_APPLESEED_ROOT}/bin
PYTHONPATH +:= scripts
APPLESEED_SEARCHPATH +:= ${REZ_APPLESEED_ROOT}/shaders
MAYA_PRESET_PATH +:= presets
MAYA_CUSTOM_TEMPLATE_PATH +:= scripts/appleseedMaya/AETemplates
MAYA_SHELF_PATH +:= prefs/shelves
MAYA_RENDER_DESC_PATH +:= renderDesc
XBMLANGPATH +:= icons/%B
EOF
