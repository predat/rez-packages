CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)


set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url https://www.python.org/ftp/python/${version}/Python-${version}.tgz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd $(MAKE) install)
else()
    set(install_cmd "")
endif()


if($ENV{REZ_BUILD_VERSION} STREQUAL "release")
    set(configure_cmd ./configure
        --prefix=${CMAKE_INSTALL_PREFIX}
        --enable-shared
        --enable-ipv6
        #--with-system-expat
        #--with-system-ffi
        #--with-system-libmpdec
        --with-dbmliborder=gdbm:ndbm
        --enable-loadable-sqlite-extensions 
        --with-ensurepip=install
        --enable-optimizations
        #--enable-profiling
        --with-computed-gotos
        --with-lto
        --with-tzpath=/usr/share/zoneinfo 
	#LIBMPDEC_CFLAGS=-I$ENV{REZ_MPDECIMAL_ROOT}/include
	#LIBMPDEC_LDFLAGS=-L$ENV{REZ_MPDECIMAL_ROOT}/lib\ -lmpdec
        LDFLAGS=-Wl,-rpath,"\$$ORIGIN/../lib/"
        )
    set(make_cmd $(MAKE) VERBOSE=1 -s -j${ncpus})
else()
    set(configure_cmd ./configure
        --prefix=${CMAKE_INSTALL_PREFIX}
        --enable-shared
        --enable-ipv6
        --with-ensurepip=install
        --with-pydebug
	# --with-system-expat
        # --with-system-ffi
        # --with-system-libmpdec
        --with-dbmliborder=gdbm:ndbm
        --enable-loadable-sqlite-extensions 
        --with-ensurepip=install
        --with-computed-gotos
        --with-tzpath=/usr/share/zoneinfo 
	#LIBMPDEC_CFLAGS=-I$ENV{REZ_MPDECIMAL_ROOT}/include
	#LIBMPDEC_LDFLAGS=-L$ENV{REZ_MPDECIMAL_ROOT}/lib\ -lmpdec
        LDFLAGS=-Wl,-rpath,'\$\$ORIGIN/../lib/')
    set(make_cmd $(MAKE) -j${ncpus})
endif()


ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    #PATCH_COMMAND $ENV{REZ_BUILD_SOURCE_PATH}/patch_ssl.sh
    #UPDATE_COMMAND rm -rf Modules/zlib
    #       COMMAND rm -rf Modules/expat
    #       COMMAND rm -rf Modules/_ctypes/{darwin,libffi}*
    #       COMMAND rm -rf Modules/_decimal/libmpdec
    CONFIGURE_COMMAND ${configure_cmd}
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ${make_cmd}
    INSTALL_COMMAND "${install_cmd}"
)



INSTALL(CODE "message(STATUS Running Phony install)")
