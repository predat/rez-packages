CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url https://www.python.org/ftp/python/${version}/Python-${version}.tgz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

if($ENV{REZ_PLATFORM_VERSION} STREQUAL osx)
    if($ENV{REZ_BUILD_VERSION} STREQUAL release)
        set(configure_cmd
            ./configure
            --prefix=${CMAKE_INSTALL_PREFIX}
            --with-cxx-main=clang++
            --enable-shared
            --enable-ipv6
            --enable-unicode=ucs4
            --enable-optimizations)
    else()  # debug
        set(configure_cmd
            ./configure
            CFLAGS=-DPy_DEBUG\ -DPy_TRACE_REFS
            --prefix=${CMAKE_INSTALL_PREFIX}
            --with-cxx-main=clang++
            --enable-shared
            --enable-ipv6
            --enable-unicode=ucs4
            --with-pydebug)
    endif()
else()  # linux
    if($ENV{REZ_BUILD_VERSION} STREQUAL release)
        set(configure_cmd 
            ./configure 
            --prefix=${CMAKE_INSTALL_PREFIX}
            --enable-shared
            --enable-ipv6
            --enable-unicode=ucs4
            # --enable-optimizations
            LDFLAGS=-Wl,-rpath,'\$\$ORIGIN/../lib/'
            CXX=g++)
    else()  # debug
        set(configure_cmd ./configure
            CFLAGS=-DPy_DEBUG\ -DPy_TRACE_REFS
            --prefix=${CMAKE_INSTALL_PREFIX}
            --enable-shared
            --enable-ipv6
            --enable-unicode=ucs4
            LDFLAGS=-Wl,-rpath,'\$\$ORIGIN/../lib/'
            --with-pydebug
            CXX=g++)
    endif()
endif()


ExternalProject_add(
    python
    URL ${url}
    PREFIX python
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND "${configure_cmd}"
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j ${ncpus}
)

install(CODE "message(STATUS Running Phony install)")
