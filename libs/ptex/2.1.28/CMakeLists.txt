CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(ExternalProject)


set(ptex_version ${PTEX_VERSION})
set(url_ptex https://github.com/wdas/ptex/archive/v${ptex_version}.zip)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ptex
    URL ${url_ptex}
    PREFIX ptex
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    ALWAYS 1
)


rez_install_files(
    cmake/ptex.cmake
    DESTINATION .
)
