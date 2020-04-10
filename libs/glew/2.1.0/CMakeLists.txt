CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(version ${GLEW_VERSION})
set(url https://downloads.sourceforge.net/project/glew/glew/${version}/glew-${version}.tgz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make GLEW_DEST="${CMAKE_INSTALL_PREFIX}" -j$ENV{REZ_BUILD_THREAD_COUNT} install)
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    glew
    URL ${url}
    PREFIX glew
    PATCH_COMMAND sh -c "patch -p1 < ${CMAKE_SOURCE_DIR}/glew-lib.patch"
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
