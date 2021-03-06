CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(ilmbase_version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url_ilmbase http://download.savannah.nongnu.org/releases/openexr/ilmbase-${ilmbase_version}.tar.gz)
set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ilmbase
    URL ${url_ilmbase}
    PREFIX ilmbase
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --with-pic --disable-debug --enable-namespaceversioning=no
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)


rez_install_files(
    cmake/ilmbase.cmake
    DESTINATION .
)
