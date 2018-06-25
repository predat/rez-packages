CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(pyside_version $ENV{REZ_BUILD_PROJECT_VERSION})

set(url_pyside https://github.com/pyside/Tools/archive/${pyside_version}.tar.gz)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    pyside-tools
    URL ${url_pyside}
    PREFIX pyside
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DShiboken_DIR=$ENV{REZ_SHIBOKEN_ROOT}/lib/cmake/Shiboken-$ENV{REZ_SHIBOKEN_VERSION}
    -DPySide_DIR=$ENV{REZ_PYSIDE_ROOT}/lib/cmake/PySide-$ENV{REZ_PYSIDE_VERSION}
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j ${ncpus}
    INSTALL_COMMAND "${install_cmd}"
)
