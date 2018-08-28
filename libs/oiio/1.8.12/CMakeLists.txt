CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


rez_find_packages(PREFIX pkgs AUTO)


set(oiio_version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url_oiio https://github.com/OpenImageIO/oiio.git)
set(tag_oiio Release-${oiio_version})


if(${REZ_BUILD_INSTALL})
    set(install_cmd make -j12 ${make_args})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DVERBOSE=ON
    -DOPENEXR_HOME=$ENV{REZ_OPENEXR_ROOT}
    -DILMBASE_INCLUDE_PATH=$ENV{REZ_OPENEXR_ROOT}/include
    -DOPENEXR_INCLUDE_PATH=$ENV{REZ_OPENEXR_ROOT}/include
    -DUSE_PYTHON=ON
    -DPYTHON_EXECUTABLE=$ENV{REZ_PYTHON_ROOT}/bin/python2.7
    -DPYTHON_LIBRARIES=${python_LIBRARIES}
    -DOCIO_PATH=$ENV{REZ_OCIO_ROOT}
    -DUSE_JPEGTURBO=ON
    -DJPEGTURBO_PATH=$ENV{REZ_JPEG_ROOT}
    -DOIIO_BUILD_TESTS=OFF
    -DZLIB_LIBRARY=${zlib_LIBRARIES}
    -DZLIB_INCLUDE_DIR=${zlib_INCLUDE_DIRS}
    -DPNG_PNG_INCLUDE_DIR=${png_INCLUDE_DIRS}
    -DPNG_LIBRARY=${png_LIBRARIES}
    -DTIFF_INCLUDE_DIR=${tiff_INCLUDE_DIRS}
    -DTIFF_LIBRARY=${tiff_LIBRARIES}
    # -DFFMPEG_AVCODEC_INCLUDE_DIR=$ENV{REZ_FFMPEG_ROOT}/include
    # -DFFMPEG_LIBAVCODEC=$ENV{REZ_FFMPEG_ROOT}/lib/libavcodec.so
    # -DFFMPEG_LIBAVFORMAT=$ENV{REZ_FFMPEG_ROOT}/lib/libavformat.so
    # -DFFMPEG_LIBAVUTIL=$ENV{REZ_FFMPEG_ROOT}/lib/libavutil.so
    # -DFFMPEG_LIBSWSCALE=$ENV{REZ_FFMPEG_ROOT}/lib/libswscale.so
    #-USE_PTEX=ON
    #-DPTEX_INCLUDE_DIR=${ptex_INCLUDE_DIRS}
    #-DPTEX_LIBRARY=${ptex_LIBRARIES}
    # -DNuke_ROOT=$ENV{REZ_NUKE_ROOT}/nuke
    # -DNUKE_DDIMAGE_LIBRARY=$ENV{REZ_NUKE_ROOT}/nuke/libDDImage.so
    # -DNUKE_INCLUDE_DIRS=$ENV{REZ_NUKE_ROOT}/nuke/include
    # -DNUKE_LIBRARY_DIRS=$ENV{REZ_NUKE_ROOT}/nuke/lib
    # -DNUKE_EXECUTABLE=$ENV{REZ_NUKE_ROOT}/Nuke$ENV{REZ_NUKE_MAJOR_VERSION}.$ENV{REZ_NUKE_MINOR_VERSION}
    -DUSE_OPENGL=OFF
    -DUSE_QT=OFF
    -DOIIO_BUILD_TESTS=OFF
    -DINSTALL_DOCS=OFF
)


ExternalProject_add(
    oiio
    GIT_REPOSITORY ${url_oiio}
    GIT_TAG ${tag_oiio}
    PREFIX oiio
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMMAND "${install_cmd}"
)


rez_install_files(
    cmake/oiio.cmake
    DESTINATION .
)
