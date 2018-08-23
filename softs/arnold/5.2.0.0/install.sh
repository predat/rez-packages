#!/bin/bash


ARNOLD_VERSION=${REZ_BUILD_PROJECT_VERSION}
INSTALL_FILE="/prod/prod2/Projets/RESSOURCES/_LIB/INSTALLS/clean/arnold/sdk/Arnold-${ARNOLD_VERSION}-linux.tgz"


# extract archive content
tar -xf "${INSTALL_FILE}" -C "${REZ_BUILD_INSTALL_PATH}"

