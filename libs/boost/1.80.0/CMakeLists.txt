CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# We split the Boost version string in multiple ones.
string(REPLACE "." ";" BOOST_VERSION_LIST ${REZ_BUILD_PROJECT_VERSION})
list(GET BOOST_VERSION_LIST 0 BOOST_VERSION_MAJOR)
list(GET BOOST_VERSION_LIST 1 BOOST_VERSION_MINOR)
list(GET BOOST_VERSION_LIST 2 BOOST_VERSION_PATCH)

# We create a version of Boost to make it match with the one in the archive name.
set(BOOST_ARCHIVE_VERSION "${BOOST_VERSION_MAJOR}_${BOOST_VERSION_MINOR}_${BOOST_VERSION_PATCH}")

# Boost
rez_set_archive(
    BOOST_URL boost/boost_${BOOST_ARCHIVE_VERSION}.tar.gz
    https://sourceforge.net/projects/boost/files/boost/${REZ_BUILD_PROJECT_VERSION}/boost_${BOOST_ARCHIVE_VERSION}.tar.gz/download
)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/boost/${REZ_BUILD_PROJECT_VERSION})
set(BUILD_DIR ${EXTRACT_DIR}/build)

# We configure/build/install Boost through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_BOOST
    URL ${BOOST_URL}
    PREFIX boost
    SOURCE_DIR ${EXTRACT_DIR}
    PATCH_COMMAND ""
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND bash ${CMAKE_SOURCE_DIR}/configure.sh ${EXTRACT_DIR}
    BUILD_COMMAND bash ${CMAKE_SOURCE_DIR}/build.sh ${EXTRACT_DIR} ${BUILD_DIR}
    INSTALL_COMMAND bash ${CMAKE_SOURCE_DIR}/install.sh ${EXTRACT_DIR} ${BUILD_DIR}
)

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] Boost-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
