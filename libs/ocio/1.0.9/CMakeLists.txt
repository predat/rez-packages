CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(ocio_version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url_ocio https://github.com/imageworks/OpenColorIO.git)
set(tag_ocio v${ocio_version})


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ocio
    GIT_REPOSITORY ${url_ocio}
    GIT_TAG ${tag_ocio}
    PREFIX ocio
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DPYTHON_INCLUDE_DIR=${python_INCLUDE_DIRS}
    -DPYTHON_LIBRARY=${python_LIBRARY}
    INSTALL_COMMAND "${install_cmd}"
    # ALWAYS 1
)


rez_install_files(
    cmake/ocio.cmake
    DESTINATION .
)
