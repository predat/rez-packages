CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(x265_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_x265 x265/x265_${x265_version}.tar.gz
    https://bitbucket.org/multicoreware/x265/downloads/x265_${x265_version}.tar.gz
)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    x265
    URL ${url_x265}
    PREFIX x265
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake
    -DVERBOSE=ON
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    ../x265/source
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 0
    BUILD_COMMAND make -j8 ${make_args}
)
