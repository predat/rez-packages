CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url_pkg https://github.com/Psyop/Cryptomatte/archive/${version}.tar.gz)


ExternalProject_add(
    ${name}
    URL ${url_pkg}
    PREFIX ${name}
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ""
)


install(
    DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/${name}/src/${name}/nuke"
    DESTINATION ${CMAKE_INSTALL_PREFIX}
)
