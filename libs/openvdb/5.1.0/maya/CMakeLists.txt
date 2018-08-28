CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/dreamworksanimation/openvdb/archive/v${version}.tar.gz)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    PREFIX ${name}
    URL ${url}
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DOPENVDB_BUILD_CORE=OFF
    -DOPENVDB_BUILD_PYTHON_MODULE=OFF
    -DOPENVDB_BUILD_MAYA_PLUGIN=ON
    -DOPENVDB_LOCATION=$ENV{REZ_OPENVDB_ROOT}
    -DILMBASE_LOCATION=$ENV{REZ_OPENEXR_ROOT}
    -DIlmbase_IEX_LIBRARY=$ENV{REZ_OPENEXR_ROOT}/lib/libIex.so
    -DIlmbase_ILMTHREAD_LIBRARY=$ENV{REZ_OPENEXR_ROOT}/lib/libIlmThread.so
    -DCMAKE_CXX_FLAGS=-std=c++11
    -DBoost_USE_STATIC_LIBS=ON
    -DOPENVDB_BUILD_UNITTESTS=OFF
    -DOPENVDB_ABI_VERSION_NUMBER=3
    -DOPENVDB_MAYA_INSTALL_BASE_DIR=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
)
