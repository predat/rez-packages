CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(ocio_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_ocio ocio/v${ocio_version}.tar.gz
    https://github.com/imageworks/OpenColorIO/archive/v${ocio_version}.tar.gz
)


if(${REZ_BUILD_INSTALL})
    #set(install_cmd make install)
    set(install_cmd cd src/nuke && make install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    ocio
    URL ${url_ocio}
    PREFIX ocio
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake
    -DVERBOSE=ON
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DCMAKE_CXX_FLAGS="-I$ENV{ILMBASE_INCLUDE_DIR}"
    -DNuke_INCLUDE_DIR=$ENV{Nuke_ROOT}/include
    -DNuke_LIBRARIES=$ENV{Nuke_ROOT}/lib
    -DGLEW_INCLUDES=$ENV{REZ_GLEW_ROOT}/include/GL
    -DGLEW_LIBRARIES=$ENV{REZ_GLEW_ROOT}/lib64/libGLEW.so
    -DILMBASE_INCLUDE_PATH=$ENV{ILMBASE_INCLUDE_DIR}
    -DOPENEXR_INCLUDE_PATH=$ENV{OPENEXR_INCLUDE_DIR}
    -DOIIO_PATH=$ENV{REZ_OIIO_ROOT}
    ../ocio
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 0
    BUILD_COMMAND make -j ${ncpus}
)

