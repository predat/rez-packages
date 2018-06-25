CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(url_pkg https://github.com/anderslanglands/alShaders2/releases/download/2.0.0-beta4/alShaders-linux-2.0.0b4-ai5.0.1.0.tar.gz)

set(name $ENV{REZ_BUILD_PROJECT_NAME})

ExternalProject_add(
    ${name}
    URL ${url_pkg}
    PREFIX ${name}
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ""
)


install(
    DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/${name}/src/${name}/ae"
    DESTINATION ${CMAKE_INSTALL_PREFIX}
)

install(
    DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/${name}/src/${name}/aexml"
    DESTINATION ${CMAKE_INSTALL_PREFIX}
)

install(
    DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/${name}/src/${name}/bin"
    DESTINATION ${CMAKE_INSTALL_PREFIX}
)
