CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)


set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version $ENV{REZ_BUILD_PROJECT_VERSION})
#set(url https://download.qt.io/archive/qt/5.15/${version}/single/qt-everywhere-src-${version}.tar.xz)
set(url https://download.qt.io/archive/qt/5.15/5.15.8/single/qt-everywhere-opensource-src-5.15.8.tar.xz)


ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    CONFIGURE_COMMAND ../qt/configure
    -prefix $ENV{REZ_BUILD_INSTALL_PATH}
    -c++std c++14
    -opensource -confirm-license
    -release
    -strip
    BUILD_COMMAND $(MAKE) -j${ncpus}
    INSTALL_COMMAND $(MAKE) install
)


INSTALL(CODE "message(STATUS Running Phony install)")
