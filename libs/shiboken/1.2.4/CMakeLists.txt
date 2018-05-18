CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

rez_find_packages(PREFIX pkgs AUTO)

# debug
get_cmake_property(_variableNames VARIABLES)
foreach (_variableName ${_variableNames})
    message(STATUS "${_variableName}=${${_variableName}}")
endforeach()

set(PYTHON_INCLUDE_DIR ${PYTHON_INCLUDEDIR})

set(shiboken_version $ENV{REZ_BUILD_PROJECT_VERSION})

#rez_set_archive(
#    url_shiboken shiboken/${shiboken_version}.tar.gz
#    https://github.com/pyside/Shiboken/archive/${shiboken_version}.tar.gz
#)

set(url_shiboken https://github.com/PySide/Shiboken.git)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    shiboken
    #URL ${url_shiboken}
    GIT_REPOSITORY ${url_shiboken}
    GIT_TAG ${shiboken_version}
    PREFIX shiboken
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DPYTHON_LIBRARY=$ENV{REZ_PYTHON_ROOT}/lib/libpython$ENV{REZ_PYTHON_MAJOR_VERSION}.$ENV{REZ_PYTHON_MINOR_VERSION}.so.1.0
    -DQT_ROOT=${REZ_QT_ROOT} ../shiboken
    BUILD_IN_SOURCE 0
    #BINARY_DIR ${CMAKE_INSTALL_PREFIX}
    BUILD_COMMAND make -j ${ncpus} VERBOSE=on
    INSTALL_COMMAND "${install_cmd}"
)

rez_install_files(
    cmake/shiboken.cmake
    DESTINATION .
)
