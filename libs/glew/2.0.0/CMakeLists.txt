CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(glew_version ${GLEW_VERSION})
set(url_glew https://downloads.sourceforge.net/project/glew/glew/${glew_version}/glew-${glew_version}.tgz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make GLEW_DEST="${CMAKE_INSTALL_PREFIX}" -j$ENV{REZ_BUILD_THREAD_COUNT} install)
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    glew
    URL ${url_glew}
    PREFIX glew
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND "${install_cmd}"
    ALWAYS 1
    BUILD_IN_SOURCE 1
)


install(
    FILES cmake/glew.cmake
    DESTINATION cmake
)
