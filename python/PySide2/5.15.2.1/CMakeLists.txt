CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)


set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version ${REZ_BUILD_PROJECT_VERSION})
set(url https://code.qt.io/pyside/pyside-setup.git)

set(CMAKE_VERBOSE_MAKEFILE ON)

if($ENV{REZ_BUILD_VERSION} STREQUAL "debug")
    set(debug_flags --debug --limited-api=no)
else()
    set(debug_flags --standalone --limited-api=yes)
endif()


ExternalProject_add(
    ${name}
    GIT_REPOSITORY ${url}
    GIT_TAG v${version}
    #URL ${url}
    GIT_PROGRESS 1
    GIT_SHALLOW 1
    PREFIX ${name}
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    BUILD_IN_SOURCE 1
    INSTALL_COMMAND PYTHONPATH=$ENV{REZ_BUILD_INSTALL_PATH}:$ENV{PYTHONPATH}
    python$ENV{REZ_PYTHON_MAJOR_VERSION} setup.py install
    -j ${ncpus}
    ${debug_flags}
    --skip-docs
    --ignore-git
    --reuse-build
    --openssl=$ENV{REZ_OPENSSL_PATH}
    --prefix=$ENV{REZ_BUILD_INSTALL_PATH}
)

ExternalProject_add(
    clean
    DEPENDS ${name}
    PREFIX clean
    DOWNLOAD_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND mv
        $ENV{REZ_BUILD_INSTALL_PATH}/lib/python$ENV{REZ_PYTHON_MAJOR_VERSION}.$ENV{REZ_PYTHON_MINOR_VERSION}/site-packages
        $ENV{REZ_BUILD_INSTALL_PATH}/python
    COMMAND rm -rf $ENV{REZ_BUILD_INSTALL_PATH}/lib
    COMMAND rm -rf $ENV{REZ_BUILD_INSTALL_PATH}/python/site-packages
)


INSTALL(CODE "message(STATUS Running Phony install)")
