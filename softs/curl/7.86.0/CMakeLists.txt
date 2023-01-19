CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url https://github.com/${name}/${name})

string(REPLACE "." ";" VERSION_LIST ${version})
list(GET VERSION_LIST 0 MAJOR)
list(GET VERSION_LIST 1 MINOR)
list(GET VERSION_LIST 2 PATCH)

ExternalProject_add(
    ${name}
    GIT_REPOSITORY ${url}
    GIT_TAG ${name}-${MAJOR}_${MINOR}_${PATCH}
    GIT_PROGRESS 1
    GIT_SHALLOW 1
    PREFIX ${name}
    CMAKE_ARGS
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DCMAKE_INSTALL_LIBDIR=lib
    -DBUILD_TESTING=OFF
)


INSTALL(CODE "message(STATUS Running Phony install)")
