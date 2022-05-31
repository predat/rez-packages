CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# We split the GLFW version string in multiple ones.
string(REPLACE "." ";" GLFW_VERSION_LIST ${REZ_BUILD_PROJECT_VERSION})
list(GET GLFW_VERSION_LIST 0 GLFW_VERSION_MAJOR)
list(GET GLFW_VERSION_LIST 1 GLFW_VERSION_MINOR)
list(GET GLFW_VERSION_LIST 2 GLFW_VERSION_PATCH)

# We create a version of PySide2 to make it match with the one in the archive name.
set(GLFW_ARCHIVE_VERSION "${GLFW_VERSION_MAJOR}.${GLFW_VERSION_MINOR}")

# GLFW
rez_set_archive(
    GLFW_URL glfw/glfw-${GLFW_ARCHIVE_VERSION}.tar.gz
    https://github.com/glfw/glfw/archive/${GLFW_ARCHIVE_VERSION}.tar.gz
)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/glfw/${REZ_BUILD_PROJECT_VERSION})
set(BUILD_DIR ${EXTRACT_DIR}/build)

# We configure/build/install GLFW through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_GLFW
    URL ${GLFW_URL}
    PREFIX glfw
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
        COMMAND echo \"\n[CMAKE] GLFW-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
