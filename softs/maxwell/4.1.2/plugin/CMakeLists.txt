CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(maxwell_version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url_maxwell ${CMAKE_CURRENT_SOURCE_DIR}/../archives/maxwell-maya-linux-${maxwell_version}.zip)


set(build_cmd ${CMAKE_CURRENT_SOURCE_DIR}/extract.sh  ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR} )


if(${REZ_BUILD_INSTALL})
    set(install_cmd ${CMAKE_CURRENT_SOURCE_DIR}/install.sh  ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX} ${MAXWELL_MAJOR_VERSION})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    maxwell
    URL ${url_maxwell}
    PREFIX maxwell
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ${build_cmd}
    INSTALL_COMMAND ${install_cmd}
    BUILD_IN_SOURCE 0
)
