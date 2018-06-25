CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


rez_find_packages(PREFIX pkgs AUTO)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/ImageEngine/cortex.git)
set(tag ${version})


if(${REZ_BUILD_INSTALL})
    set(install_cmd make -j24 install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    GIT_REPOSITORY ${url}
    GIT_TAG ${tag}
    PREFIX ${name}
    #PATCH_COMMAND sh -c " echo $PWD && sed -i 's/tracelite/trace/g' SConstruct"
    PATCH_COMMAND sh -c "patch -p1 < ${CMAKE_SOURCE_DIR}/cortex-usd.patch"
    CONFIGURE_COMMAND ""
    BUILD_COMMAND sh -c "echo \"---------------$ENV{REZ_BOOST_ROOT} \" && scons -j13 --debug=explain install \
    INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} \
    INSTALL_PYTHON_DIR=${CMAKE_INSTALL_PREFIX}/python \
    BOOST_INCLUDE_PATH=$ENV{REZ_BOOST_ROOT}/include \
    BOOST_LIB_PATH=$ENV{REZ_BOOST_ROOT}/lib \
    BOOST_LIB_SUFFIX='' \
    TBB_INCLUDE_PATH=$ENV{REZ_TBB_ROOT}/include \
    TBB_LIB_PATH=$ENV{REZ_TBB_ROOT}/lib \
    OIIO_INCLUDE_PATH=$ENV{REZ_OIIO_ROOT}/include \
    OIIO_LIB_PATH=$ENV{REZ_OIIO_ROOT}/lib64 \
    OSL_INCLUDE_PATH=$ENV{REZ_OSL_ROOT}/include \
    OSL_LIB_PATH=$ENV{REZ_OSL_ROOT}/lib \
    OPENEXR_INCLUDE_PATH=$ENV{REZ_OPENEXR_ROOT}/include \
    OPENEXR_LIB_PATH=$ENV{REZ_OPENEXR_ROOT}/lib \
    ILMBASE_INCLUDE_PATH=$ENV{REZ_OPENEXR_ROOT}/include \
    ILMBASE_LIB_PATH=$ENV{REZ_OPENEXR_ROOT}/lib \
    BLOSC_INCLUDE_PATH=$ENV{REZ_BLOSC_ROOT}/include \
    BLOSC_LIB_PATH=$ENV{REZ_BLOSC_ROOT}/lib \
    GLEW_INCLUDE_PATH=$ENV{REZ_GLEW_ROOT}/include \
    GLEW_LIB_PATH=$ENV{REZ_GLEW_ROOT}/lib64 \
    USD_INCLUDE_PATH=$ENV{REZ_USD_ROOT}/include \
    USD_LIB_PATH=$ENV{REZ_USD_ROOT}/lib \
    ALEMBIC_INCLUDE_PATH=$ENV{REZ_ALEMBIC_ROOT}/include \
    ALEMBIC_LIB_PATH=$ENV{REZ_ALEMBIC_ROOT}/lib \
    HDF5_INCLUDE_PATH=$ENV{REZ_HDF5_ROOT}/include \
    HDF5_LIB_PATH=$ENV{REZ_HDF5_ROOT}/lib \
    WITH_GL=1 \
    USE_PTHREADS=1 \
    MAYA_ROOT=$ENV{REZ_MAYA_ROOT}/maya \
    MAYA_ADLM_ENV_FILE=$ENV{REZ_MAYA_ROOT}/AdlmThinClientCustomEnv.xml \
    NUKE_ROOT=$ENV{REZ_NUKE_ROOT}/nuke \
    ARNOLD_ROOT=$ENV{REZ_ARNOLD_ROOT} \
    # HOUDINI_ROOT=$ENV{REZ_HOUDINI_ROOT}/houdini"
    BUILD_IN_SOURCE 1
    #INSTALL_COMMAND "${install_cmd}"
    INSTALL_COMMAND ""
)


#rez_install_files(
#   HOUDINI_ROOT cmake/ocio.cmake
#    DESTINATION .
#)
