CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)


rez_find_packages(PREFIX pkgs AUTO)


set(tiff_version ${TIFF_VERSION})
set(url_tiff http://download.osgeo.org/libtiff/tiff-${tiff_version}.tar.gz)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make -j ${ncpu} install ${make_args})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DZLIB_INCLUDE_DIR=${zlib_INCLUDE_DIRS}
    -DZLIB_LIBRARY=${zlib_LIBRARIES}
    -DJPEG_INCLUDE_DIR=${jpeg_INCLUDE_DIRS}
    -DJPEG_LIBRARY=${jpeg_LIBRARIES}
)


ExternalProject_add(
    tiff
    URL ${url_tiff}
    PREFIX tiff
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS} -DCMAKE_POSITION_INDEPENDENT_CODE=ON
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
)


install(
    FILES cmake/tiff.cmake
    DESTINATION cmake
)
