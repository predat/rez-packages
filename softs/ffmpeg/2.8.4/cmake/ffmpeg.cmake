find_package(PkgConfig)

set( ENV{PKG_CONFIG_PATH} $ENV{PKG_CONFIG_PATH}:$ENV{REZ_FFMPEG_ROOT}/lib/pkgconfig)

if(ffmpeg_COMPONENTS)
    set(FFMPEG_COMPONENTS ${ffmpeg_COMPONENTS})
endif()

message(STATUS "FFMEG_COMPONENTS: ${FFMPEG_COMPONENTS}")

pkg_check_modules(FFMPEG REQUIRED ${FFMPEG_COMPONENTS})

set(ffmpeg_INCLUDE_DIRS     ${FFMPEG_INCLUDE_DIRS})
set(ffmpeg_LIBRARY_DIRS     ${FFMPEG_LIBRARY_DIRS})
set(ffmpeg_LIBRARIES ${FFMPEG_LIBRARIES})
