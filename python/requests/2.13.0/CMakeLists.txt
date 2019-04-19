CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})

if(NOT ${REZ_BUILD_INSTALL})
    message(FATAL_ERROR "Must install this package with -i flag")
endif()

set(url https://github.com/kennethreitz/requests.git)
set(tag ${version})

set(src_path ${CMAKE_BINARY_DIR}/requests/src/requests)

if(${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    set(install_cmd bash ${CMAKE_SOURCE_DIR}/install.sh ${src_path} ${CMAKE_INSTALL_PREFIX})
endif()

ExternalProject_add(
    requests
    GIT_REPOSITORY ${url}
    GIT_TAG v${tag}
    PREFIX requests
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ""
    INSTALL_COMMAND "${install_cmd}"
)

install(CODE "message(STATUS Running Phony install)")
