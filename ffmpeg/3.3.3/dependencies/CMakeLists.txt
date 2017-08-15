# Set config wrapper variables
configure_file(configure_wrapper.in configure_wrapper @ONLY)

# Source url's
set(url_yasm git://github.com/yasm/yasm.git)
set(url_nasm http://www.nasm.us/pub/nasm/releasebuilds/2.13.01/nasm-2.13.01.tar.gz)
set(url_x264 git://git.videolan.org/x264)
set(url_x265 https://bitbucket.org/multicoreware/x265)
set(url_fdk-aac git://git.code.sf.net/p/opencore-amr/fdk-aac)
set(url_lame http://downloads.sourceforge.net/project/lame/lame/3.99/lame-3.99.5.tar.gz)
set(url_opus git://git.opus-codec.org/opus.git)
set(url_ogg http://downloads.xiph.org/releases/ogg/libogg-1.3.2.tar.gz)
set(url_vorbis http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.4.tar.gz)
set(url_vpx https://chromium.googlesource.com/webm/libvpx.git)

#
# YASM
#
ExternalProject_add(
    yasm
    GIT_REPOSITORY ${url_yasm}
    PREFIX yasm
    UPDATE_COMMAND ./autogen.sh
    CONFIGURE_COMMAND ${conf_wrapper} ./configure --prefix=${DEP_ROOT}
    INSTALL_COMMAND make install
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ${conf_wrapper} make
)

#
# NASM
#
ExternalProject_add(
    nasm
    URL ${url_nasm}
    PREFIX nasm
    UPDATE_COMMAND ./autogen.sh
    CONFIGURE_COMMAND ${conf_wrapper} ./configure --prefix=${DEP_ROOT}
    INSTALL_COMMAND make install
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ${conf_wrapper} make
)

#
# x264
#
ExternalProject_add(
    x264
    DEPENDS nasm
    GIT_REPOSITORY ${url_x264}
    PREFIX x264
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ${conf_wrapper} ./configure --prefix=${DEP_ROOT} --enable-pic --enable-static
    INSTALL_COMMAND make install
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ${conf_wrapper} make
)

#
# x265
#
ExternalProject_add(
    x265
    DEPENDS yasm
    HG_REPOSITORY ${url_x265}
    PREFIX x265
    UPDATE_COMMAND echo add_subdirectory(source) > CMakeLists.txt
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${DEP_ROOT} -DCMAKE_PROJECT_NAME=x265 -DENABLE_SHARED:bool=off -DENABLE_PIC=ON
    BUILD_COMMAND make
    BUILD_IN_SOURCE 0
    INSTALL_COMMAND make install
)

#
# fdk-aac
#
ExternalProject_add(
    fdk-aac
    GIT_REPOSITORY ${url_fdk-aac}
    PREFIX fdk-aac
    UPDATE_COMMAND autoreconf -fiv
    CONFIGURE_COMMAND ${conf_wrapper} ./configure --prefix=${DEP_ROOT} --disable-shared
    INSTALL_COMMAND make install
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ${conf_wrapper} make
)

#
# lame
#
ExternalProject_add(
    lame
    URL ${url_lame}
    PREFIX lame
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ${conf_wrapper} ./configure --prefix=${DEP_ROOT} --disable-shared --enable-nasm
    INSTALL_COMMAND make install
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ${conf_wrapper} make
)

#
# opus
#
ExternalProject_add(
    opus
    GIT_REPOSITORY ${url_opus}
    PREFIX opus
    UPDATE_COMMAND autoreconf -fiv
    CONFIGURE_COMMAND ${conf_wrapper} ./configure --prefix=${DEP_ROOT} --disable-shared
    INSTALL_COMMAND make install
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ${conf_wrapper} make
)

#
# ogg
#
ExternalProject_add(
    ogg
    URL ${url_ogg}
    PREFIX ogg
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ${conf_wrapper} ./configure --prefix=${DEP_ROOT} --disable-shared
    INSTALL_COMMAND make install
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ${conf_wrapper} make
)

#
# vorbis
#
ExternalProject_add(
    vorbis
    DEPENDS ogg
    URL ${url_vorbis}
    PREFIX vorbis
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ${conf_wrapper} ./configure --prefix=${DEP_ROOT} --with-ogg=${DEP_ROOT} --disable-shared
    INSTALL_COMMAND make install
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ${conf_wrapper} make
)

#
# vpx
#
ExternalProject_add(
    vpx
    DEPENDS yasm
    GIT_REPOSITORY ${url_vpx}
    PREFIX vpx
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ${conf_wrapper} ./configure --prefix=${DEP_ROOT} --disable-examples --enable-pic
    INSTALL_COMMAND make install
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ${conf_wrapper} make
)
