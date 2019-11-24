CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/AcademySoftwareFoundation/openexr/archive/v${version}.tar.gz)
set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)


if(${REZ_BUILD_INSTALL})
    set(install_cmd cd PyIlmBase && make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    UPDATE_COMMAND cd PyIlmBase && ./bootstrap
    CONFIGURE_COMMAND cd PyIlmBase && export CXXFLAGS=-O3 && ./configure
    --prefix=${CMAKE_INSTALL_PREFIX}
    --enable-cxxstd=14
    --enable-shared
    --enable-static
    --with-pic
    --with-boost-include-dir=$ENV{REZ_BOOST_ROOT}/include
    --with-boost-lib-dir=$ENV{REZ_BOOST_ROOT}/lib
    --with-boost-python-libname=boost_python$ENV{REZ_PYTHON_MAJOR_VERSION}$ENV{REZ_PYTHON_MINOR_VERSION}
    LDFLAGS=-Wl,-rpath,$ENV{REZ_BOOST_ROOT}/lib
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND cd PyIlmBase && make ${make_args}
)

install(CODE "message(STATUS Running Phony install)")
