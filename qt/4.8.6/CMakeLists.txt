CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(qt_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_qt qt/qt-everywhere-opensource-src-${qt_version}.tar.gz
    https://download.qt.io/archive/qt/4.8/${qt_version}/qt-everywhere-opensource-src-${qt_version}.tar.gz
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    qt
    URL ${url_qt}
    PREFIX qt
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure -confirm-license -opensource -no-qt3support -opengl -no-rpath -ptmalloc -optimized-qmake -fast --prefix=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j8
)
