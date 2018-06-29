CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(version $ENV{REZ_BUILD_PROJECT_VERSION})

set(url
    https://github.com/imageworks/OpenShadingLanguage/archive/Release-${version}.tar.gz )

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install VERBOSE=1)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    osl
    URL ${url}
    PREFIX osl
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DBUILD_TESTING=OFF
    -DSTOP_ON_WARNING=OFF
    -DOSL_BUILD_PLUGINS=OFF
    -DOSL_BUILD_TESTS=OFF
    -DENABLERTTI=ON
    -DOSL_BUILD_CPP11=1
    -DILMBASE_HOME=$ENV{REZ_OPENEXR_ROOT}
    #-DILMBASE_CUSTOM_LIBRARIES='Half;Iex;Imath;IlmThread'
    -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
    -DOPENIMAGEIOHOME=$ENV{REZ_OIIO_ROOT}
    -DLLVM_VERSION=3.4.2
    -DLLVM_DIRECTORY=$ENV{REZ_LLVM_ROOT}
    -DLLVM_STATIC=ON
    -DUSE_fPIC=ON
    #-DUSE_LLVM_BITCODE:BOOL=0  # FIXME: compile clang with llvm
    -DVERBOSE=ON
    ../osl
    BUILD_IN_SOURCE 0
    BUILD_COMMAND make -j ${ncpus}
    INSTALL_COMMAND "${install_cmd}"
)
