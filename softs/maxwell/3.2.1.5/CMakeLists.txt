CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(url_maxwell_studio
    /prod/prod2/Projets/RESSOURCES/_LIB/INSTALLS/clean/maxwell/Maxwell3/${MAXWELL_VERSION}/maxwell-${MAXWELL_VERSION}-Linux64.tar.gz)

set(install_cmd ${CMAKE_CURRENT_SOURCE_DIR}/install.sh
    ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX} ${MAXWELL_VERSION})


ExternalProject_add(
    maxwell_studio
    URL ${url_maxwell_studio}
    PREFIX maxwell
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ${install_cmd} maxwell_studio
    BUILD_IN_SOURCE 1
)
