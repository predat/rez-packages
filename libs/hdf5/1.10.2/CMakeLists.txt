CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url https://www.hdfgroup.org/ftp/HDF5/releases/hdf5-${version}/src/hdf5-${version}.tar.gz)
set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT})


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    hdf5
    URL ${url}
    PREFIX hdf5
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --with-pic
    --enable-build-mode=production --enable-cxx
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)


install(
    FILES cmake/hdf5.cmake
    DESTINATION cmake
)
