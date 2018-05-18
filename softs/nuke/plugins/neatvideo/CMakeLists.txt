CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(ExternalProject)


set(url_pkg
    /prod/prod2/Projets/RESSOURCES/_LIB/INSTALLS/clean/neat_video/${REZ_BUILD_PROJECT_VERSION}/NeatVideoOFX.Intel64.tgz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    neatvideo
    URL ${url_pkg}
    PREFIX neatvideo
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/install.sh ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX}
    BUILD_IN_SOURCE 0
)

