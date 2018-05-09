CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(url_muster
    #http://www.tweaksoftware.com/static/downloads/rv-Linux-x86-64-${MUSTER_VERSION}.tar.gz)
    ${CMAKE_CURRENT_SOURCE_DIR}/archives/Muster${MUSTER_VERSION}.x64.linux.tar.gz)

set(install_cmd ${CMAKE_CURRENT_SOURCE_DIR}/install.sh
    ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX} ${MUSTER_MAJOR_VERSION})


ExternalProject_add(
    muster
    URL ${url_muster}
    PREFIX muster
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    INSTALL_COMMAND ${install_cmd}
    BUILD_COMMAND ""
    BUILD_IN_SOURCE 1
)
