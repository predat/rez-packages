CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(url_pkg https://github.com/anderslanglands/alShaders2/releases/download/2.0.0-beta4/alShaders-linux-2.0.0b4-ai5.0.1.0.tar.gz)


ExternalProject_add(
    $ENV{REZ_BUILD_PROJECT_NAME}
    URL ${url_pkg}
    PREFIX $ENV{REZ_BUILD_PROJECT_NAME}
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ""
)


install(
    DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/cryptomatte/src/cryptomatte/ae"
    DESTINATION ${CMAKE_INSTALL_PREFIX}
)

install(
    DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/cryptomatte/src/cryptomatte/aexml"
    DESTINATION ${CMAKE_INSTALL_PREFIX}
)

install(
    DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/cryptomatte/src/cryptomatte/bin"
    DESTINATION ${CMAKE_INSTALL_PREFIX}
)
