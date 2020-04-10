CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(version ${PNG_VERSION})
set(url https://download.sourceforge.net/libpng/libpng-${version}.tar.gz)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    png
    URL ${url}
    PREFIX png
    CMAKE_ARGS
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DCMAKE_POSITION_INDEPENDENT_CODE=ON
    -DCMAKE_INSTALL_LIBDIR=lib
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 0
)

install(
    FILES cmake/png.cmake
    DESTINATION cmake
)
