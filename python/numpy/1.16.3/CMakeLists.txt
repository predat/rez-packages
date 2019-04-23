CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(pkg_name $ENV{REZ_BUILD_PROJECT_NAME})

if(NOT ${REZ_BUILD_INSTALL})
    message(FATAL_ERROR "Must install this package with -i flag")
endif()

set(url https://github.com/${pkg_name}/${pkg_name}.git)
set(tag v${version})

set(src_path ${CMAKE_BINARY_DIR}/${pkg_name}/src/${pkg_name})

if(${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    set(install_cmd bash ${CMAKE_SOURCE_DIR}/install.sh ${src_path} ${CMAKE_INSTALL_PREFIX})
endif()

ExternalProject_add(
    ${pkg_name}
    GIT_REPOSITORY ${url}
    GIT_TAG ${tag}
    PREFIX ${pkg_name}
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ""
    INSTALL_COMMAND "${install_cmd}"
)

install(CODE "message(STATUS Running Phony install)")
