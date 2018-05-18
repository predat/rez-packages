#!/bin/bash

YETI_VERSION=${REZ_BUILD_PROJECT_VERSION}
INSTALL="/prod/prod2/Projets/RESSOURCES/_LIB/INSTALLS/clean/yeti/${YETI_VERSION}/Yeti-v${YETI_VERSION}_Maya${MAYA_VERSION}-linux64.tar.gz"

tar -xvf "${INSTALL}" --strip 1 -C "${REZ_BUILD_INSTALL_PATH}"

sed -i 's/path_to_yeti_root/./g' "${REZ_BUILD_INSTALL_PATH}/pgYetiMaya.mod"
