CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)

rez_find_packages(PREFIX pkgs AUTO)


set(openexr_version ${OPENEXR_VERSION})
set(url_openexr https://github.com/openexr/openexr.git)
set(tag_openexr v${openexr_version})

if(${REZ_BUILD_INSTALL})
    set(install_cmd make -j ${ncpu} install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
  openexr
  GIT_REPOSITORY ${url_openexr}
  GIT_TAG ${tag_openexr}
  PREFIX openexr
  UPDATE_COMMAND ""
  CONFIGURE_COMMAND ""
  BUILD_COMMAND ""
  INSTALL_COMMAND ""
)

ExternalProject_add(
    ilmbase
    DEPENDS openexr
    PREFIX ilmbase
    DOWNLOAD_COMMAND ""
    SOURCE_DIR ${PROJECT_BINARY_DIR}/openexr/src/openexr/IlmBase
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DNAMESPACE_VERSIONING=OFF
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 0
)

ExternalProject_add(
    openexr_build
    DEPENDS ilmbase
    DOWNLOAD_COMMAND ""
    PREFIX openexr_build
    SOURCE_DIR ${PROJECT_BINARY_DIR}/openexr/src/openexr/OpenEXR
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DNAMESPACE_VERSIONING=OFF -DILMBASE_PACKAGE_PREFIX=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 0
    BUILD_COMMAND make -j ${ncpu} ${make_args}
)

#ExternalProject_add(
#    pyilmbase
#    DEPENDS ilmbase
#    DOWNLOAD_COMMAND ""
#    PREFIX pyilmbase
#    SOURCE_DIR ${PROJECT_BINARY_DIR}/openexr/src/openexr/PyIlmBase
#    UPDATE_COMMAND ./bootstrap
#    CONFIGURE_COMMAND LD_LIBRARY_PATH=${CMAKE_INSTALL_PREFIX}/lib ./configure
#    --prefix=${CMAKE_INSTALL_PREFIX}
#    -with-ilmbase-prefix=${CMAKE_INSTALL_PREFIX}
#    --with-boost-include-dir=$ENV{REZ_BOOST_ROOT}/include
#    --with-boost-lib-dir=$ENV{REZ_BOOST_ROOT}/lib
#    --disable-ilmbasetest
#    --disable-boostpythontest
#    INSTALL_COMMAND "${install_cmd}"
#    BUILD_IN_SOURCE 1
#    BUILD_COMMAND VERBOSE=1 make -j ${ncpu} ${make_args}
#)


rez_install_files(
    cmake/openexr.cmake
    DESTINATION .
)
