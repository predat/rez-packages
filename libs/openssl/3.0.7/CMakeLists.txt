CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://www.openssl.org/source/${name}-${version}.tar.gz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd $(MAKE) install ${make_args})
else()
    set(install_cmd "")
endif()


set(configure_cmd ./config
    --prefix=${CMAKE_INSTALL_PREFIX}
    --libdir=lib
    --with-zlib-include=$ENV{REZ_ZLIB_ROOT}/include
    --with-zlib-lib=$ENV{REZ_ZLIB_ROOT}/lib
    -Wl,-rpath='\$$ORIGIN/../lib')
    #shared zlib-dynamic)


ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND "${configure_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND $(MAKE)
    INSTALL_COMMAND "${install_cmd}"
)


INSTALL(CODE "message(STATUS Running Phony install)")
