CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

rez_find_packages(PREFIX pkgs AUTO)

set(oiio_version $ENV{REZ_BUILD_PROJECT_VERSION})

#rez_set_archive(
#    url_oiio oiio/Release-${oiio_version}.tar.gz
#    https://github.com/OpenImageIO/oiio/archive/Release-${oiio_version}.tar.gz
#)

set(url_oiio https://github.com/OpenImageIO/oiio.git)
set(tag_oiio Release-${oiio_version})

# Create a wrapper script for cmake commands
set(PKG_CONFIG_PATH $ENV{PKG_CONFIG_PATH})
configure_file(configure_wrapper.in configure_wrapper @ONLY)
set(conf_wrapper ${PROJECT_BINARY_DIR}/configure_wrapper)


#if(${REZ_BUILD_INSTALL})
#    set(install_cmd make install)
#else()
#    set(install_cmd "")
#endif()


ExternalProject_add(
    oiio
    #URL ${url_oiio}
    GIT_REPOSITORY ${url_oiio}
    GIT_TAG ${tag_oiio}
    PREFIX oiio
    #UPDATE_COMMAND ""
    #CONFIGURE_COMMAND cmake
    #-DNuke_ROOT=$ENV{Nuke_ROOT}
    #-DVERBOSE=ON
    #-DGLEW_INCLUDES=$ENV{REZ_GLEW_ROOT}/include/GL
    #-DGLEW_LIBRARIES=$ENV{REZ_GLEW_ROOT}/lib64/libGLEW.so
    #-DPYTHON_LIBRARY=$ENV{REZ_PYTHON_ROOT}/lib/libpython$ENV{REZ_PYTHON_MAJOR_VERSION}.$ENV{REZ_PYTHON_MINOR_VERSION}.so.1.0
    #-DPYTHON_INCLUDE_DIR=$ENV{REZ_PYTHON_ROOT}/include/python$ENV{REZ_PYTHON_MAJOR_VERSION}.$ENV{REZ_PYTHON_MINOR_VERSION}
    #-DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    #-DILMBASE_INCLUDE_PATH=$ENV{ILMBASE_INCLUDE_DIR}
    #-DOPENEXR_INCLUDE_PATH=$ENV{OPENEXR_INCLUDE_DIR}
    #../oiio
    #INSTALL_COMMAND "${install_cmd}"
    CMAKE_COMMAND ${conf_wrapper} cmake
    CMAKE_ARGS
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DVERBOSE=ON
    -DILMBASE_HOME=$ENV{REZ_ILMBASE_ROOT}
    -DOPENEXR_HOME=$ENV{REZ_OPENEXR_ROOT}
    -DPYTHON_HOME=$ENV{REZ_PYTHON_ROOT}
    -DOCIO_PATH=$ENV{REZ_OCIO_ROOT}
    BUILD_IN_SOURCE 0
    #BUILD_COMMAND make -j ${ncpus}
)

rez_install_files(
    cmake/oiio.cmake
    DESTINATION .
)
