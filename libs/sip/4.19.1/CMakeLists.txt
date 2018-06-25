CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


rez_find_packages(PREFIX pkgs AUTO)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url
    https://sourceforge.net/projects/pyqt/files/sip/sip-${version}/sip-${version}.tar.gz)


ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    CONFIGURE_COMMAND python configure.py -b ${CMAKE_INSTALL_PREFIX}/bin -d
    ${CMAKE_INSTALL_PREFIX}/lib/python2.7/site-packages -e
    ${CMAKE_INSTALL_PREFIX}/include/python2.7 -v
    ${CMAKE_INSTALL_PREFIX}/share/sip
    BUILD_COMMAND make
    BUILD_IN_SOURCE 1
    INSTALL_COMMAND make install
    # ALWAYS 1
)


#rez_install_files(
#    cmake/ocio.cmake
#    DESTINATION .
#)
