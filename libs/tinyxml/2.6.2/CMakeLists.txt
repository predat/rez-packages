CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# We split the TinyXML version string in multiple ones.
string(REPLACE "." ";" TINYXML_VERSION_LIST ${REZ_BUILD_PROJECT_VERSION})
list(GET TINYXML_VERSION_LIST 0 TINYXML_VERSION_MAJOR)
list(GET TINYXML_VERSION_LIST 1 TINYXML_VERSION_MINOR)
list(GET TINYXML_VERSION_LIST 2 TINYXML_VERSION_PATCH)

# We create a version of TinyXML to make it match with the one in the archive name.
set(TINYXML_ARCHIVE_VERSION "${TINYXML_VERSION_MAJOR}_${TINYXML_VERSION_MINOR}_${TINYXML_VERSION_PATCH}")

# TinyXML
rez_set_archive(
    TINYXML_URL tinyxml/tinyxml_${TINYXML_ARCHIVE_VERSION}.tar.gz
    https://sourceforge.net/projects/tinyxml/files/tinyxml/2.6.2/tinyxml_${TINYXML_ARCHIVE_VERSION}.tar.gz/download
)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/tinyxml/${REZ_BUILD_PROJECT_VERSION})
set(BUILD_DIR ${EXTRACT_DIR}/build)

# We configure/build/install TinyXML through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_TINYXML
    URL ${TINYXML_URL}
    PREFIX tinyxml
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
        COMMAND echo \"\n[CMAKE] TinyXML-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
