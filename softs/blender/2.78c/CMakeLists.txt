CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

rez_find_packages(PREFIX pkgs AUTO)

set(blender_version $ENV{REZ_BUILD_PROJECT_VERSION})

#rez_set_archive(
#    url_blender blender/blender-${blender_version}.tar.gz
#    https://github.com/glfw/glfw/archive/${glfw_version}.tar.gz
#)

set(url_blender https://git.blender.org/blender.git)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    blender
    #URL ${url_blender}
    GIT_REPOSITORY ${url_blender}
    GIT_TAG v${blender_version}
    PREFIX blender
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DGLEW_INCLUDE_DIR=$ENV{GLEW_INCLUDE_DIR}
    -DGLEW_LIBRARY=$ENV{GLEW_LIBRARY}
    -DWITH_SYSTEM_GLEW=OFF
    -DOPENEXR_INCLUDE_DIR=$ENV{REZ_OPENEXR_ROOT}/include
    -DOPENEXR_HALF_LIBRARY=$ENV{REZ_ILMBASE_ROOT}/lib/libHalf.so
    -DOPENEXR_IEX_LIBRARY=$ENV{REZ_ILMBASE_ROOT}/lib/libIex.so
    -DOPENEXR_ILMIMF_LIBRARY=$ENV{REZ_OPENEXR_ROOT}/lib/libIlmImf.so
    -OPENEXR_ILMTHREAD_LIBRARY=$ENV{REZ_ILMBASE_ROOT}/lib/libIlmThread.so
    -DOPENEXR_IMATH_LIBRARY=$ENV{REZ_ILMBASE_ROOT}/lib/libImath.so
    -DOPENIMAGEIO_INCLUDE_DIR=$ENV{REZ_OIIO_ROOT}/include
    -DOPENIMAGEIO_LIBRARY=$ENV{REZ_OIIO_ROOT}/lib/libOpenImageIO.so

    ../blender
    INSTALL_COMMAND "${install_cmd}"
    BUILD_COMMAND make -j ${ncpus}
)
