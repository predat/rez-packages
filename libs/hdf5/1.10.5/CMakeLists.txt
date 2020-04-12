CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(short_version ${HDF5_MAJOR_VERSION}.${HDF5_MINOR_VERSION})
set(url https://support.hdfgroup.org/ftp/HDF5/releases/${name}-${short_version}/${name}-${version}/src/${name}-${version}.tar.bz2)
set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure
    --prefix=${CMAKE_INSTALL_PREFIX}
    --with-pic
    --enable-build-mode=production
    --enable-optimization=high
    --enable-cxx
    INSTALL_COMMAND "${install_cmd}"
    BUILD_COMMAND make ${make_args}
    BUILD_IN_SOURCE 1
)

install(CODE "message(STATUS Running Phony install)")
