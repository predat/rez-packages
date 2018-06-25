CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


rez_find_packages(PREFIX pkgs AUTO)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/LumaPictures/usd-arnold)
#set(tag ${version})


if(${REZ_BUILD_INSTALL})
    set(install_cmd make ${make_args})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
    -DUSD_ROOT=$ENV{REZ_USD_ROOT}
    -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
    -DARNOLD_HOME=$ENV{REZ_ARNOLD_ROOT}
    -DUSD_ARNOLD_INCLUDE_DIR=$ENV{REZ_USD_ARNOLD_ROOT}/include
    -DUSD_ARNOLD_LIBRARY=$ENV{REZ_USD_ARNOLD_ROOT}/lib
    -DMTOA_LOCATION=$ENV{REZ_MTOA_ROOT}
    -DTBB_ROOT_DIR=$ENV{REZ_TBB_ROOT}
    -DTBB_INCLUDE_DIR=$ENV{REZ_TBB_ROOT}/include
    -DTBB_LIBRARY=$ENV{REZ_TBB_ROOT}/lib
    -DTBB_tbb_LIBRARY=$ENV{REZ_TBB_ROOT}/lib/libtbb.so
    -DBUILD_USD_PLUGIN=OFF
    -DBUILD_USD_MAYA_PLUGIN=ON
    -DPXR_BUILD_TESTS=OFF
)


ExternalProject_add(
    ${name}
    GIT_REPOSITORY ${url}
    #GIT_TAG ${tag}
    PREFIX ${name}
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMMAND "${install_cmd}"
)

