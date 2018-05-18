CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)


set(python_version $ENV{REZ_BUILD_PROJECT_VERSION})

set(url_python https://www.python.org/ftp/python/${python_version}/Python-${python_version}.tgz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    python
    URL ${url_python}
    PREFIX python
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --enable-shared --enable-ipv6 --enable-unicode=ucs4
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j ${ncpus}
)


rez_install_files(
    cmake/python.cmake
    DESTINATION .
)

