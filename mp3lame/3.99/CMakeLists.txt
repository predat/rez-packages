CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(mp3lame_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_mp3lame mp3lame/lame-3.99.5.tar.gz
    http://downloads.sourceforge.net/project/lame/lame/3.99/lame-3.99.5.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    mp3lame
    URL ${url_mp3lame}
    PREFIX mp3lame
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)
