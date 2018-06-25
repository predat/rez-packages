CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

rez_find_packages(PREFIX pkgs AUTO)

set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://code.qt.io/pyside/pyside-setup.git)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    GIT_REPOSITORY ${url}
    #GIT_TAG ${version}
    GIT_TAG 6d8dee0
    PREFIX ${name}
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_IN_SOURCE 1
    BUILD_COMMAND python setup.py --ignore-git --jobs 12 install
    INSTALL_COMMAND ""
)

# rez_install_files(
#    cmake/pyside.cmake
#    DESTINATION .
# )
