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
    URL https://github.com/alembic/alembic/archive/1.7.12.tar.gz
    PREFIX alembic
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DUSE_HDF5=ON
    -DHDF5_ROOT=$ENV{REZ_HDF5_ROOT}
    -DILMBASE_ROOT=$ENV{REZ_ILMBASE_ROOT}
    #-DILMBASE_INCLUDE_DIR=$ENV{REZ_OPENEXR_ROOT}/include/OpenEXR
    -DALEMBIC_LIB_USES_BOOST=ON
    -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
    -DALEMBIC_PYILMBASE_INCLUDE_DIRECTORY=$ENV{REZ_PYILMBASE_ROOT}/include/OpenEXR
    -DALEMBIC_PYIMATH_MODULE_DIRECTORY=$ENV{REZ_PYILMBASE_ROOT}/lib/python$ENV{REZ_PYTHON_MAJOR_VERSION}.$ENV{REZ_PYTHON_MINOR_VERSION}/site-packages
    -DUSE_TESTS=OFF
    -DUSE_BINARIES=ON
    -DUSE_PYALEMBIC=ON
    -DUSE_STATIC_HDF5=ON
    -DALEMBIC_ILMBASE_LINK_STATIC=ON
    -DCMAKE_VERBOSE_MAKEFILE=ON
    INSTALL_COMMAND "${install_cmd}"
    # ALWAYS 1
)

install(CODE "message(STATUS Running Phony install)")
