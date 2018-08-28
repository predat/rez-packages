CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)


set(qt_version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url_qt https://download.qt.io/archive/qt/5.11/${qt_version}/single/qt-everywhere-src-${qt_version}.tar.xz)


ExternalProject_add(
    qt
    URL ${url_qt}
    PREFIX qt
    UPDATE_COMMAND gcc --version
    CONFIGURE_COMMAND /bin/sh ${CMAKE_CURRENT_SOURCE_DIR}/wrapper.sh ./configure
    -confirm-license -opensource -release -opengl
    -nomake tests -nomake examples
    -skip wayland -skip webengine
    -no-rpath
    -prefix ${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND make install
    BUILD_IN_SOURCE 1
    BUILD_COMMAND /bin/sh ${CMAKE_CURRENT_SOURCE_DIR}/wrapper.sh make -j ${ncpus}
)

