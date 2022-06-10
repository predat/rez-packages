CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# We split the Qt version string in multiple ones.
string(REPLACE "." ";" QT_VERSION_LIST ${REZ_BUILD_PROJECT_VERSION})
list(GET QT_VERSION_LIST 0 QT_MAJOR_VERSION)
list(GET QT_VERSION_LIST 1 QT_MINOR_VERSION)
list(GET QT_VERSION_LIST 2 QT_PATCH_VERSION)

# Qt
rez_set_archive(
    QT_URL qt/qt-everywhere-src-${REZ_BUILD_PROJECT_VERSION}.tar.xz
    http://download.qt.io/official_releases/qt/${QT_MAJOR_VERSION}.${QT_MINOR_VERSION}/${REZ_BUILD_PROJECT_VERSION}/single/qt-everywhere-src-${REZ_BUILD_PROJECT_VERSION}.tar.xz
)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/qt/${REZ_BUILD_PROJECT_VERSION})
set(BUILD_DIR ${EXTRACT_DIR}/build)

# We configure/build/install Qt through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_QT
    URL ${QT_URL}
    PREFIX qt
    SOURCE_DIR ${EXTRACT_DIR}
    PATCH_COMMAND ""
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND bash ${CMAKE_SOURCE_DIR}/configure.sh ${EXTRACT_DIR} ${BUILD_DIR}
    BUILD_COMMAND bash ${CMAKE_SOURCE_DIR}/build.sh ${BUILD_DIR}
    INSTALL_COMMAND bash ${CMAKE_SOURCE_DIR}/install.sh ${BUILD_DIR}
)

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] Qt-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
