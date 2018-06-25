CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)



if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    qt
    GIT_REPOSITORY https://github.com/autodesk-forks/qtbase.git
    GIT_TAG autodesk/vfx/5.6.1/maya/2018/update3
    PREFIX qt
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure
    -prefix ${CMAKE_INSTALL_PREFIX}
    -confirm-license
    -opensource
    -release
    -no-rpath
    -no-gtkstyle
    -no-audio-backend
    #-no-dbus
    -opengl
    #-skip qtconnectivity
    #-skip qtwebengine
    #-skip qt3d
    #-skip qtdeclarative
    -no-libudev
    -no-icu
    -qt-pcre
    -qt-xcb
    -nomake tests
    -nomake examples

    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j ${ncpus}
)

