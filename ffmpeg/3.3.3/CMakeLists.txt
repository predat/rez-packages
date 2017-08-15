CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(openexr_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_ffmpeg ffmpeg/ffmpeg-${openexr_version}.tar.bz2
    http://ffmpeg.org/releases/ffmpeg-3.3.3.tar.bz2
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    ffmpeg
    URL ${url_ffmpeg}
    PREFIX ffmpeg
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --enable-gpl --enable-libmp3lame --enable-libx264 --enable-libx265 --enable-nonfree
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)

rez_install_files(
    cmake/ffmpeg.cmake
    DESTINATION .
)
