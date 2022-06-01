CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# embree
rez_set_archive(
    EMBREE_URL embree/embree-${REZ_BUILD_PROJECT_VERSION}.tar.gz
    https://github.com/embree/embree/releases/download/v${REZ_BUILD_PROJECT_VERSION}/embree-${REZ_BUILD_PROJECT_VERSION}.x86_64.linux.tar.gz
)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/embree/${REZ_BUILD_PROJECT_VERSION})

# We configure/build/install embree through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_EMBREE
    URL ${EMBREE_URL}
    PREFIX embree
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
    COMMAND echo \"\n[CMAKE] EMBREE-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
