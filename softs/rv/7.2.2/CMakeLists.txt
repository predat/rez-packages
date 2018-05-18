CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(url_rv http://www.tweaksoftware.com/static/downloads/rv-Linux-x86-64-${RV_VERSION}.tar.gz)

set(install_cmd ${CMAKE_CURRENT_SOURCE_DIR}/install.sh
    ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX} ${RV_MAJOR_VERSION})


ExternalProject_add(
    rv
    URL ${url_rv}
    PREFIX rv
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    INSTALL_COMMAND ${install_cmd}
    BUILD_COMMAND ""
    BUILD_IN_SOURCE 1
)
