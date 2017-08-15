CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(ffmpeg_version ${FFMPEG_VERSION})

set(url_ffmpeg http://ffmpeg.org/releases/ffmpeg-${ffmpeg_version}.tar.bz2)

#set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT})
set(make_args)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

# Create a wrapper script for configure commands
set(DEP_ROOT ${PROJECT_BINARY_DIR}/DEPENDENCIES_PREFIX)
set(PKG_CONFIG_PATH "${DEP_ROOT}/lib/pkgconfig")
set(PATH "${DEP_ROOT}/bin:$ENV{PATH}")
configure_file(dependencies/configure_wrapper.in configure_wrapper @ONLY)
set(conf_wrapper ${PROJECT_BINARY_DIR}/configure_wrapper)

add_subdirectory(dependencies)

ExternalProject_add(
    ffmpeg
    DEPENDS yasm x264 x265 fdk-aac lame opus ogg vorbis vpx
    URL ${url_ffmpeg}
    PREFIX ffmpeg
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ${conf_wrapper} ./configure --prefix=${CMAKE_INSTALL_PREFIX} --extra-cflags="-I${DEPROOT}/include" --extra-ldflags="-L${DEPROOT}/lib" --pkg-config-flags=--static --enable-shared --disable-static --enable-pic --enable-gpl --enable-nonfree --enable-libfdk-aac --enable-libfreetype --enable-libmp3lame --enable-libopus --enable-libvorbis --enable-libvpx --enable-libx264 --enable-libx265
    INSTALL_COMMAND ${install_cmd}
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ${conf_wrapper} make
)

rez_install_files(
    cmake/ffmpeg.cmake
    DESTINATION .
)

if(${REZ_BUILD_INSTALL})
  install (SCRIPT "${CMAKE_SOURCE_DIR}/dependencies/PostInstall.cmake")
endif()
