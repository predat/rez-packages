CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# We split the Doxygen version string in multiple ones.
string(REPLACE "." ";" DOXYGEN_VERSION_LIST ${REZ_BUILD_PROJECT_VERSION})
list(GET DOXYGEN_VERSION_LIST 0 DOXYGEN_VERSION_MAJOR)
list(GET DOXYGEN_VERSION_LIST 1 DOXYGEN_VERSION_MINOR)
list(GET DOXYGEN_VERSION_LIST 2 DOXYGEN_VERSION_PATCH)

# We create a version of Doxygen to make it match with the one in the archive name.
set(DOXYGEN_ARCHIVE_VERSION "${DOXYGEN_VERSION_MAJOR}_${DOXYGEN_VERSION_MINOR}_${DOXYGEN_VERSION_PATCH}")

# Doxygen
rez_set_archive(
    DOXYGEN_URL doxygen/doxygen-Release_${DOXYGEN_ARCHIVE_VERSION}.tar.gz
    https://github.com/doxygen/doxygen/archive/Release_${DOXYGEN_ARCHIVE_VERSION}.tar.gz
)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/doxygen/${REZ_BUILD_PROJECT_VERSION})
set(BUILD_DIR ${EXTRACT_DIR}/build)

# We configure/build/install Doxygen through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_DOXYGEN
    URL ${DOXYGEN_URL}
    PREFIX doxygen
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
        COMMAND echo \"\n[CMAKE] Doxygen-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
