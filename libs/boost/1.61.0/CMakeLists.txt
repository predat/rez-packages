CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(boost_version $ENV{REZ_BUILD_PROJECT_VERSION})

set(url_boost http://downloads.sourceforge.net/project/boost/boost/1.61.0/boost_1_61_0.tar.gz)

set(b2_args -j ${ncpus} -q -s NO_BZIP2=1 --prefix=${CMAKE_INSTALL_PREFIX}
    --exec-prefix=${CMAKE_INSTALL_PREFIX} link=shared link=static --toolset=gcc
    cxxflags=-fPIC\ -std=c++11 )

if(${REZ_BUILD_INSTALL})
    set(install_cmd ./b2 install ${b2_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    boost
    URL ${url_boost}
    PREFIX boost
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./bootstrap.sh
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ./b2 ${b2_args}
)

rez_install_files(
    cmake/boost.cmake
    DESTINATION .
)
