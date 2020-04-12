CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)


set(name $ENV{REZ_BUILD_PROJECT_VERSION})
set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(short_version ${QT_MAJOR_VERSION}.${QT_MINOR_VERSION})
set(url https://download.qt.io/archive/qt/${short_version}/${version}/single/qt-everywhere-src-${version}.tar.xz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    URL ${url}
    URL_MD5 7c04c678d4ecd9e9c06747e7c17e0bb9
    PREFIX ${name}
    #UPDATE_COMMAND export
    CONFIGURE_COMMAND ./configure 
    -confirm-license 
    -opensource
    -release 
    -nomake tests
    -nomake examples
    -opengl
    -openssl-linked
    -c++std c++14
    -system-zlib
    -system-pcre
    -system-freetype
    -system-libpng
    -system-libjpeg
    -system-tiff
    -system-xcb
    -system-harfbuzz
    -webengine-pulseaudio
    -webengine-alsa
    -prefix ${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j ${ncpus}
)

install(CODE "message(STATUS Running Phony install)")
