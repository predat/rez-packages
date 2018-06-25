CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)



if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    alembic
    URL https://github.com/alembic/alembic/archive/1.7.8.tar.gz
    PREFIX alembic
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DUSE_HDF5=ON
    -DHDF5_ROOT=$ENV{REZ_HDF5_ROOT}
    -DALEMBIC_LIB_USES_BOOST=ON
    -DILMBASE_ROOT=$ENV{REZ_OPENEXR_ROOT}
    -DILMBASE_INCLUDE_DIR=$ENV{REZ_OPENEXR_ROOT}/include/OpenEXR
    -DUSE_TESTS=OFF
    -DUSE_BINARIES=OFF
    -DVERBOSE=1
    INSTALL_COMMAND "${install_cmd}"
    # ALWAYS 1
)

