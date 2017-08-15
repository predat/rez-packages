CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(openexr_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_x264 x264/last_stable_x264.tar.bz2
    ftp://ftp.videolan.org/pub/videolan/x264/snapshots/last_stable_x264.tar.bz2
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    x264
    URL ${url_x264}
    PREFIX x264
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --with-pic --enable-shared --enable-static
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)
