CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

rez_find_packages(PREFIX pkgs AUTO)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url http://github.com/shotgunsoftware/python-api)
set(src_path ${CMAKE_BINARY_DIR}/shotgunapi/src/shotgunapi)

if(${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    set(install_cmd bash ${CMAKE_SOURCE_DIR}/install.sh ${src_path} ${CMAKE_INSTALL_PREFIX})
endif()


if(NOT ${REZ_BUILD_INSTALL})
    message(FATAL_ERROR "Must install this package with -i flag")
endif()


ExternalProject_add(
    shotgunapi
    GIT_REPOSITORY ${url}
    GIT_TAG v${version}
    PREFIX shotgunapi
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ""
    INSTALL_COMMAND "${install_cmd}"
)
