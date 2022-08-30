CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# We split the TBB version string in multiple ones.
string(REPLACE "." ";" TBB_VERSION_LIST ${REZ_BUILD_PROJECT_VERSION})
list(GET TBB_VERSION_LIST 0 TBB_VERSION_MAJOR)
list(GET TBB_VERSION_LIST 1 TBB_VERSION_MINOR)

# We create a version of PySide2 to make it match with the one in the archive name.
set(TBB_ARCHIVE_VERSION "${TBB_VERSION_MAJOR}_${TBB_VERSION_MINOR}")

# TBB
rez_set_archive(
    TBB_URL /tbb/tbb-v${TBB_VERSION_MAJOR}.${TBB_VERSION_MINOR}.tar.gz
    https://github.com/oneapi-src/oneTBB/archive/refs/tags/v2020.3.tar.gz
)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/tbb/${REZ_BUILD_PROJECT_VERSION})

# We configure/build/install TBB through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_TBB
    URL ${TBB_URL}
    PREFIX tbb
    SOURCE_DIR ${EXTRACT_DIR}
    PATCH_COMMAND ""
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND bash ${CMAKE_SOURCE_DIR}/install.sh ${EXTRACT_DIR}
)

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] TBB-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)

