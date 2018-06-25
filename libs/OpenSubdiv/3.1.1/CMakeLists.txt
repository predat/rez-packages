CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(opensubdiv_version $ENV{REZ_BUILD_PROJECT_VERSION})


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    opensubdiv
    URL https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v3_1_1.tar.gz
    PREFIX opensubdiv
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DNO_EXAMPLES=ON
    -DNO_TUTORIALS=ON
    -DNO_DOC=ON
    -DNO_OMP=ON
    -DNO_DX=ON
    -DNO_TESTS=ON
    -DNO_CUDA=ON
    -DNO_OPENCL=ON
    -DGLEW_LOCATION=$ENV{REZ_GLEW_ROOT}
    -DTBB_LOCATION=$ENV{REZ_TBB_ROOT}
    -DPTEX_LOCATION=$ENV{REZ_PTEX_ROOT}
    INSTALL_COMMAND "${install_cmd}"
    # ALWAYS 1
)


#rez_install_files(
#    cmake/ocio.cmake
#    DESTINATION .
#)
