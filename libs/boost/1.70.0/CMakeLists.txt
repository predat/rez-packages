CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url http://downloads.sourceforge.net/project/boost/boost/${version}/boost_1_70_0.tar.gz)
set(b2_args 
    -j ${ncpus} 
    -q 
    -s NO_BZIP2=1 
    --prefix=${CMAKE_INSTALL_PREFIX}
    --exec-prefix=${CMAKE_INSTALL_PREFIX}
    --toolset=gcc
    threading=multi
    release
    link=shared link=static
    cxxflags=-fPIC\ -std=c++14)


if(${REZ_BUILD_INSTALL})
    set(install_cmd ./b2 install ${b2_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    UPDATE_COMMAND ""
    #CONFIGURE_COMMAND ./bootstrap.sh && cp $ENV{REZ_BUILD_SOURCE_PATH}/user-config.jam $ENV{REZ_BUILD_PATH}/boost/src/boost/
    CONFIGURE_COMMAND ./bootstrap.sh && cp $ENV{REZ_BUILD_SOURCE_PATH}/user-config.jam $ENV{HOME}/
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ./b2 ${b2_args}
    INSTALL_COMMAND "${install_cmd}"
)

install(CODE "message(STATUS Running Phony install)")
