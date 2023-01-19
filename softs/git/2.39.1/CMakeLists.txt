CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)
include(ProcessorCount)

set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url https://github.com/${name}/${name})

ProcessorCount(ncpus)


ExternalProject_add(
    ${name}
    GIT_REPOSITORY ${url}
    GIT_TAG v${version}
    GIT_PROGRESS 1
    GIT_SHALLOW 1
    PREFIX ${name}
    CONFIGURE_COMMAND make configure && ./configure
    --prefix=/${CMAKE_INSTALL_PREFIX}
    --with-zlib=$ENV{REZ_ZLIB_ROOT}
    --with-openssl=$ENV{REZ_OPENSSL_ROOT}
    --with-curl=$ENV{REZ_CURL_ROOT}
    BUILD_COMMAND $(MAKE) V=1 -j${ncpus}
    INSTALL_COMMAND $(MAKE) -s install
    BUILD_IN_SOURCE 1
)


INSTALL(CODE "message(STATUS Running Phony install)")
