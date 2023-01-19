CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url_cmake https://github.com/Kitware/CMake/releases/download/v${version}/cmake-${version}.tar.gz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    ${name}
    URL ${url_cmake}
    PREFIX ${name}
    UPDATE_COMMAND ""
    CMAKE_ARGS
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DOPENSSL_USE_STATIC_LIBS=TRUE
    -DCMAKE_BUILD_TYPE=Release
    #-DBUILD_QtDialog=ON
    #-DCMAKE_USE_SYSTEM_CURL=ON
    #-DCMAKE_USE_SYSTEM_LIBLZMA=ON
    #-DCMAKE_USE_SYSTEM_ZLIB=ON
    #-DCMAKE_USE_SYSTEM_BZIP2=ON
)

INSTALL(CODE "message(STATUS Running Phony install)")
