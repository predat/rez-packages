CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(cmake_version $ENV{REZ_BUILD_PROJECT_VERSION})

set(url_cmake 
    https://cmake.org/files/v3.11/cmake-${cmake_version}.tar.gz
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    cmake
    URL ${url_cmake}
    PREFIX cmake
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND VERBOSEE=1 make -j ${ncpus}
)
