CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)


set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url https://download.qt.io/archive/qt/6.4/6.4.2/single/qt-everywhere-src-6.4.2.tar.xz)

#set(CMAKE_VERBOSE_MAKEFILE ON)
#set(TMPDIR /datas/mazieres/tmp)
#set(ENV{TMPDIR} /datas/mazieres/tmp)

ExternalProject_add(
    ${name}
    # GIT_REPOSITORY ${url}
    # GIT_TAG v${version}
    URL ${url}
    PREFIX ${name}
    CMAKE_GENERATOR Ninja
    CMAKE_ARGS
    -DCMAKE_INSTALL_PREFIX=$ENV{REZ_BUILD_INSTALL_PATH}
    -DCMAKE_BUILD_TYPE=$ENV{REZ_BUILD_VERSION}
    -DQT_BUILD_TESTS_BY_DEFAULT=OFF
    -DQT_BUILD_EXAMPLES_BY_DEFAULT=OFF
    #-DBUILD_qtlocation=OFF
    #-DBUILD_qtpositioning=OFF
    #-DBUILD_qtwebengine=OFF
    -DBUILD_qtwayland=OFF
    -DBUILD_qtmqtt=OFF
)


INSTALL(CODE "message(STATUS Running Phony install)")
