CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


#rez_find_packages(PREFIX pkgs AUTO)


set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url https://github.com/ninja-build/ninja.git)
set(tag v${version})


if(${REZ_BUILD_INSTALL})
    set(install_cmd export)
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    GIT_REPOSITORY ${url}
    GIT_TAG ${tag}
    PREFIX ${name}
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND mkdir -p ${CMAKE_INSTALL_PREFIX}/bin && cp ninja ${CMAKE_INSTALL_PREFIX}/bin
)

install(CODE "message(STATUS Running Phony install)")
