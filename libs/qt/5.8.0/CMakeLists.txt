CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)


set(qt_version $ENV{REZ_BUILD_PROJECT_VERSION})

set(
    url_qt
    https://download.qt.io/archive/qt/5.8/${qt_version}/single/qt-everywhere-opensource-src-${qt_version}.tar.gz
)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    qt
    URL ${url_qt}
    URL_MD5 a9f2494f75f966e2f22358ec367d8f41
    PREFIX qt
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure -confirm-license -opensource -release -nomake
    tests -nomake examples -opengl -skip webengine -prefix ${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j ${ncpus}
)

