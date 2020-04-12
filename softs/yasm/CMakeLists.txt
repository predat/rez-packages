CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)

rez_find_packages(PREFIX pkgs AUTO)


set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version v${REZ_BUILD_PROJECT_VERSION})
set(url https://github.com/yasm/yasm)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make -j ${ncpu} install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    GIT_REPOSITORY ${url}
    GIT_TAG ${version}
    PREFIX ${name}
    CMAKE_ARGS
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DBUILD_SHARED_LIBS=OFF
    -DYASM_BUILD_TESTS=OFF
    BUILD_IN_SOURCE 0
)


INSTALL(CODE "message(STATUS Running Phony install)")
