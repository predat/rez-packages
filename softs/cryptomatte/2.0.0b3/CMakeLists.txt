CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(url_pkg
    https://github.com/anderslanglands/alShaders2/releases/download/2.0.0-beta3/alShaders-linux-2.0.0b3-ai5.0.1.0.tar.gz)

 set(install_cmd ${CMAKE_CURRENT_SOURCE_DIR}/install.sh
    ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX})

# set(build_cmd ${CMAKE_CURRENT_SOURCE_DIR}/extract.sh
#    ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX})


ExternalProject_add(
    $ENV{REZ_BUILD_PROJECT_NAME}
    URL ${url_pkg}
    PREFIX $ENV{REZ_BUILD_PROJECT_NAME}
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ${install_cmd}
)
