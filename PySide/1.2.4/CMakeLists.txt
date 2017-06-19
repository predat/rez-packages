CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(pyside_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_pyside PySide/${pyside_version}.tar.gz
    https://github.com/pyside/pyside/archive/${pyside_version}.tar.gz
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    pyside
    URL ${url_pyside}
    PREFIX pyside
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DShiboken_DIR=$ENV{REZ_SHIBOKEN_ROOT}/lib/cmake/Shiboken-1.2.4
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j ${ncpus}
    INSTALL_COMMAND "${install_cmd}"
)
