#!/bin/bash

PKG_NAME=${REZ_BUILD_PROJECT_NAME//_maya/}
PKG_VER=${REZ_BUILD_PROJECT_VERSION//./}
OS=${REZ_PLATFORM_MAJOR_VERSION}
ARCH=${REZ_ARCH_MAJOR_VERSION//86_/}  # x86_64

PKG_INSTALL="${PKG_NAME}_adv_${PKG_VER}_maya${MAYA_VERSION}_${OS}_${ARCH}.zip"

echo "Extract archive"
unzip -q "${REZ_BUILD_SOURCE_PATH}/archives/${PKG_INSTALL}" -d "${REZ_BUILD_PATH}"

echo "Extract final archive into install directory"
unzip -q "${REZ_BUILD_PATH}/${PKG_INSTALL}" -d "${REZ_BUILD_INSTALL_PATH}"

echo "Install lic file."
cp "${REZ_BUILD_SOURCE_PATH}/config/vrlclient.xml" "${REZ_BUILD_INSTALL_PATH}"
