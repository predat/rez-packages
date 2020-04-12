CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)

#rez_find_packages(PREFIX pkgs AUTO)


set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version ${REZ_BUILD_PROJECT_VERSION})
set(url http://prdownloads.sourceforge.net/${name}/${name}-${version}.tar.gz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    CONFIGURE_COMMAND ./configure
    --prefix=${CMAKE_INSTALL_PREFIX}
    --with-python=${REZ_PYTHON_ROOT}/bin/python${REZ_PYTHON_MAJOR_VERSION}.${REZ_PYTHON_MINOR_VERSION}
    --with-boost=${REZ_BOOST_ROOT}
    --with-boost-libdir=${REZ_BOOST_ROOT}/lib
    --without-go
    --without-r
    --without-d
    --without-csharp
    --without-ruby
    --without-android
    --without-guile
    --without-java
    --without-scilab
    --without-octave
    --without-perl5
    --without-php
    --without-pcre
    --without-tcl
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ${MAKE}
    #INSTALL_COMMAND ${MAKE} install
)


INSTALL(CODE "message(STATUS Running Phony install)")
