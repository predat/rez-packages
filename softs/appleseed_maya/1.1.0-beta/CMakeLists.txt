CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})

set(url https://github.com/appleseedhq/appleseed-maya/archive/${version}.tar.gz)


if(${REZ_BUILD_INSTALL})
    #set(install_cmd make install)
    set(install_cmd ${CMAKE_CURRENT_SOURCE_DIR}/install.sh ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    appleseed_maya
    URL ${url}
    PREFIX appleseed_maya
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
    -DOSL_COMP_LIBRARY=$ENV{REZ_OSL_ROOT}/lib/liboslcomp.so
    -DOSL_QUERY_LIBRARY=$ENV{REZ_OSL_ROOT}/lib/liboslquery.so
    -DOSL_COMPILER=$ENV{REZ_OSL_ROOT}/bin/oslc
    -DOSL_QUERY_INFO=$ENV{REZ_OSL_ROOT}/bin/oslinfo
    -DOSL_INCLUDE_DIR=$ENV{REZ_OSL_ROOT}/include
    -DOSL_EXEC_LIBRARY=$ENV{REZ_OSL_ROOT}/lib/liboslexec.so
    -DAPPLESEED_INCLUDE_DIR=$ENV{REZ_APPLESEED_ROOT}/include
    -DAPPLESEED_LIBRARY=$ENV{REZ_APPLESEED_ROOT}/lib/libappleseed.so
    -DOPENIMAGEIO_INCLUDE_DIR=$ENV{REZ_OIIO_ROOT}/include
    -DOPENIMAGEIO_LIBRARY=$ENV{REZ_OIIO_ROOT}/lib64/libOpenImageIO.so
    -DIMATH_INCLUDE_DIR=$ENV{REZ_OPENEXR_ROOT}/include
    -DIMATH_HALF_LIBRARY=$ENV{REZ_OPENEXR_ROOT}/lib/libHalf.so
    -DIMATH_IEX_LIBRARY=${ENVREZ_OPENEXR_ROOT}/lib/libIex.so
    -DIMATH_MATH_LIBRARY=$ENV{REZ_OPENEXR_ROOT}/lib/libImath.so
    -DMAYA_LOCATION=$ENV{MAYA_LOCATION}
    ../appleseed_maya
    BUILD_IN_SOURCE 0
    BUILD_COMMAND make -j ${ncpus}
    INSTALL_COMMAND "${install_cmd}"
)
