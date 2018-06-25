CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


rez_find_packages(PREFIX pkgs AUTO)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url http://prdownloads.sourceforge.net/scons/scons-${version}.tar.gz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd python setup.py install --prefix=${CMAKE_INSTALL_PREFIX})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    CONFIGURE_COMMAND ""
    BUILD_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    INSTALL_COMMAND ""
    # ALWAYS 1
)
