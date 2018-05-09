CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


rez_find_packages(PREFIX pkgs AUTO)


set(oiio_version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url_oiio https://github.com/OpenImageIO/oiio.git)
set(tag_oiio Release-${oiio_version})


if(${REZ_BUILD_INSTALL})
    set(install_cmd make ${make_args})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DVERBOSE=ON
    -DILMBASE_INCLUDE_PATH=${openexr_INCLUDE_DIRS}
    -DOPENEXR_INCLUDE_PATH=${openexr_INCLUDE_DIRS}
    -DINSTALL_DOCS=OFF
    -DUSE_PYTHON=ON
    -DPYTHON_EXECUTABLE=$ENV{REZ_PYTHON_ROOT}/bin/python2.7
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
    -DUSE_OPENGL=OFF
    -DUSE_QT=OFF
    -DUSE_FFMPEG=ON
    -DFFMPEG_AVCODEC_INCLUDE_DIR=${ffmpeg_INCLUDE_DIRS}
    #-DFFMPEG_LIBRARY=${ffmpeg_LIBRARIES}
# /prod/softprod/rez-packages/ext/ffmpeg/2.8.4/platform-linux/arch-x86_64/lib/libavcodec.so;/prod/softprod/rez-packages/ext/ffmpeg/2.8.4/platform-linux/arch-x86_64/lib/libavformat.so;/prod/softprod/rez-packages/ext/ffmpeg/2.8.4/platform-linux/arch-x86_64/lib/libavutil.so;/prod/softprod/rez-packages/ext/ffmpeg/2.8.4/platform-linux/arch-x86_64/lib/libswscale.so
    
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
