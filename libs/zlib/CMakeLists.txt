CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(zlib_version ${ZLIB_VERSION})
set(url_zlib https://github.com/madler/zlib/archive/v${zlib_version}.zip)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    zlib
    URL ${url_zlib}
    PREFIX zlib
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DCCMAKE_POSITION_INDEPENDENT_CODE=ON
    INSTALL_COMMAND "${install_cmd}"
    ALWAYS 1
    BUILD_IN_SOURCE 0
)

install(
    FILES cmake/zlib.cmake
    DESTINATION cmake
)
