#!/bin/bash


if [[ "${MAYA_VERSION}" == *"ext2"* ]] ; then
    MTOA_MAYA_VERSION="20165"
else
    MTOA_MAYA_VERSION=${REZ_MAYA_MAJOR_VERSION}
fi

MTOA_VERSION=${REZ_BUILD_PROJECT_VERSION}

INSTALL="/prod/prod2/Projets/RESSOURCES/_LIB/INSTALLS/clean/arnold/mtoa/${MTOA_VERSION}/MtoA-${MTOA_VERSION}-linux-${MTOA_MAYA_VERSION}.run"

${INSTALL} --target "${REZ_BUILD_PATH}" --noexec

unzip "${REZ_BUILD_PATH}/package.zip" -d "${REZ_BUILD_INSTALL_PATH}"
