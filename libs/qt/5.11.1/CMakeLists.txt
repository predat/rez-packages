CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)


set(qt_version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url_qt https://download.qt.io/archive/qt/5.11/${qt_version}/single/qt-everywhere-src-${qt_version}.tar.xz)
set(CMAKE_C_COMPILER /opt/rh/devtoolset-4/root/usr/bin/gcc)
set(CMAKE_CXX_COMPILER /opt/rh/devtoolset-4/root/usr/bin/g++)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    qt
    URL ${url_qt}
    PREFIX qt
    UPDATE_COMMAND gcc --version
    CONFIGURE_COMMAND CXX=/opt/rh/devtoolset-4/root/usr/bin/g++ CC=/opt/rh/devtoolset-4/root/usr/bin/gcc ./configure
    -confirm-license -opensource -release -opengl
    -nomake tests -nomake examples
    -skip wayland -skip webengine
    -prefix ${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j ${ncpus}
)

