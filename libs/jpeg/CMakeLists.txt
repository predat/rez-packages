CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)


set(jpeg_version ${JPEG_VERSION})
set(url_jpeg "https://github.com/libjpeg-turbo/libjpeg-turbo/archive/${jpeg_version}.zip")

if(${REZ_BUILD_INSTALL})
    set(install_cmd make -j ${ncpu} install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    jpeg
    URL ${url_jpeg}
    PREFIX jpeg
    UPDATE_COMMAND autoreconf -ivf
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --enable-static --enable-shared
    INSTALL_COMMAND "${install_cmd}"
    ALWAYS 1
    BUILD_IN_SOURCE 1
)

install(
    FILES cmake/jpeg.cmake cmake/FindJPEG.cmake
    DESTINATION cmake
)
