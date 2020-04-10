CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)


set(name $ENV{REZ_BUILD_PROJECT_VERSION})
set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(sversion $ENV{REZ_QT_MAJOR_VERSION}.$ENV{REZ_QT_MINOR_VERSION})
set(url https://download.qt.io/archive/qt/5.12/${version}/single/qt-everywhere-src-${version}.tar.xz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    URL ${url}
    URL_MD5 ce2c5661c028b9de6183245982d7c120
    PREFIX ${name}
    #UPDATE_COMMAND export
    CONFIGURE_COMMAND ./configure 
    -confirm-license 
    -opensource
    -release 
    -nomake tests
    -nomake examples
    -opengl
    -openssl-linked
    -prefix ${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j ${ncpus}
)

install(CODE "message(STATUS Running Phony install)")
