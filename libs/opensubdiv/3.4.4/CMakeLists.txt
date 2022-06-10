CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# We split the OpenSubdiv version string in multiple ones.
string(REPLACE "." ";" OPENSUBDIV_VERSION_LIST ${REZ_BUILD_PROJECT_VERSION})
list(GET OPENSUBDIV_VERSION_LIST 0 OPENSUBDIV_VERSION_MAJOR)
list(GET OPENSUBDIV_VERSION_LIST 1 OPENSUBDIV_VERSION_MINOR)
list(GET OPENSUBDIV_VERSION_LIST 2 OPENSUBDIV_VERSION_PATCH)

# We create a version of PySide2 to make it match with the one in the archive name.
set(OPENSUBDIV_ARCHIVE_VERSION "${OPENSUBDIV_VERSION_MAJOR}_${OPENSUBDIV_VERSION_MINOR}_${OPENSUBDIV_VERSION_PATCH}")

# OpenSubdiv
rez_set_archive(
    OPENSUBDIV_URL opensubdiv/OpenSubdiv-${OPENSUBDIV_ARCHIVE_VERSION}.tar.gz
    https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v${OPENSUBDIV_ARCHIVE_VERSION}.tar.gz
)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/opensubdiv/${REZ_BUILD_PROJECT_VERSION})
set(BUILD_DIR ${EXTRACT_DIR}/build)

# We configure/build/install OpenSubdiv through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_OPENSUBDIV
    URL ${OPENSUBDIV_URL}
    PREFIX opensubdiv
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
        COMMAND echo \"\n[CMAKE] OpenSubdiv-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
