CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


rez_find_packages(PREFIX pkgs AUTO)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
#set(url https://github.com/PixarAnimationStudios/USD.git)
set(url /users/smaziere/dev/USD)
set(tag v${version})


if(${REZ_BUILD_INSTALL})
    set(install_cmd make -j24 install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    URL ${url}
    #GIT_REPOSITORY ${url}
    #GIT_TAG ${tag}
    PREFIX ${name}
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DPXR_ENABLE_PYTHON_SUPPORT=ON
    -DBUILD_SHARED_LIBS=ON
    -DPXR_BUILD_DOCUMENTATION=OFF
    -DPXR_BUILD_TESTS=OFF
    -DPXR_ENABLE_PTEX_SUPPORT=ON
    -DPXR_BUILD_EMBREE_PLUGIN=OFF
    -DPXR_BUILD_IMAGING=ON
    -DPXR_BUILD_USD_IMAGING=ON
    -DPXR_BUILD_ALEMBIC_PLUGIN=ON
    -DALEMBIC_DIR=$ENV{REZ_ALEMBIC_ROOT}
    -DOPENEXR_LOCATION=$ENV{REZ_OPENEXR_ROOT}
    -DPXR_ENABLE_HDF5_SUPPORT=ON
    -DHDF5_INCLUDE_DIRS=${hdf5_INCLUDE_DIRS}
    -DHDF5_LIBRARIES=${hdf5_LIBRARIES}
    -DHDF5_ROOT=$ENV{REZ_HDF5_ROOT}
    -DTBB_INCLUDE_DIRS=${tbb_INCLUDE_DIRS}
    -DTBB_LIBRARIES=${tbb_LIBRARIES}
    -DTBB_ROOT_DIR=$ENV{REZ_TBB_ROOT}
    -DTBB_tbb_LIBRARY_RELEASE=$ENV{REZ_TBB_ROOT}/lib/libtbb.so.2
    -DTBB_tbbmalloc_LIBRARY_RELEASE=$ENV{REZ_TBB_ROOT}/lib/libtbbmalloc.so.2
    # Maya
    -DPXR_BUILD_MAYA_PLUGIN=ON
    -DMAYA_LOCATION=$ENV{MAYA_LOCATION}
    -DMAYA_tbb_LIBRARY=$ENV{REZ_TBB_ROOT}/lib/libtbb.so.2
    -DGLEW_LOCATION=$ENV{REZ_GLEW_ROOT}
    -DOIIO_LOCATION=$ENV{REZ_OIIO_ROOT}
    -DOPENSUBDIV_ROOT_DIR=$ENV{REZ_OPENSUBDIV_ROOT}
    -DPTEX_LOCATION=$ENV{REZ_PTEX_ROOT}
    INSTALL_COMMAND "${install_cmd}"
    # ALWAYS 1
)


#rez_install_files(
#    cmake/ocio.cmake
#    DESTINATION .
#)
