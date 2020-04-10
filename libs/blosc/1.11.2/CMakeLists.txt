CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url https://github.com/Blosc/c-blosc/archive/v${version}.tar.gz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    blosc
    URL ${url}
    PREFIX blosc
    CMAKE_ARGS
    -D CMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -D BUILD_TESTS=OFF
    -D BUILD_BENCHMARKS=OFF
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 0
)

install(CODE "message(STATUS Running Phony install)")
