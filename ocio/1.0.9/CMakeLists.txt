CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(ocio_version $ENV{REZ_BUILD_PROJECT_VERSION})

#rez_set_archive(
#    url_ocio ocio/v${ocio_version}.tar.gz
#    https://github.com/imageworks/OpenColorIO/archive/v${ocio_version}.tar.gz
#)
#
set(url_ocio https://github.com/imageworks/OpenColorIO.git)
set(tag_ocio v${ocio_version})


if(${REZ_BUILD_INSTALL})
    #set(install_cmd make install)
    #set(install_cmd make install)
    set(install_cmd rez-env -i ${PROJECT_BINARY_DIR}/build.rxt -- make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    ocio
    #URL ${url_ocio}
    GIT_REPOSITORY ${url_ocio}
    GIT_TAG ${tag_ocio}
    PREFIX ocio
    #UPDATE_COMMAND ""
    #CONFIGURE_COMMAND cmake
    #-DVERBOSE=ON
    #-DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    #-DCMAKE_CXX_FLAGS="-I$ENV{ILMBASE_INCLUDE_DIR}"
    #-DGLEW_INCLUDES=$ENV{REZ_GLEW_ROOT}/include/GL
    #-DGLEW_LIBRARIES=$ENV{REZ_GLEW_ROOT}/lib64/libGLEW.so
    #-DILMBASE_INCLUDE_PATH=$ENV{ILMBASE_INCLUDE_DIR}
    #-DOPENEXR_INCLUDE_PATH=$ENV{OPENEXR_INCLUDE_DIR}
    #-DOIIO_PATH=$ENV{REZ_OIIO_ROOT}
    #../ocio
    INSTALL_COMMAND "${install_cmd}"
    #BUILD_IN_SOURCE 0
    #BUILD_COMMAND make -j ${ncpus}
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DPYTHON_INCLUDE_DIR=${PYTHON_INCLUDE_DIRS} -DPYTHON_LIBRARY=${PYTHON_LIBDIR}/lib${PYTHON_LIBRARIES}.so
)

rez_install_files(
    cmake/ocio.cmake
    DESTINATION .
)
