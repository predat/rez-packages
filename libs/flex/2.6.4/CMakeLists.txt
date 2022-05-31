CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# flex
rez_set_archive(
    FLEX_URL flex/flex-${REZ_BUILD_PROJECT_VERSION}.tar.gz
    https://github.com/westes/flex/releases/download/v${REZ_BUILD_PROJECT_VERSION}/flex-${REZ_BUILD_PROJECT_VERSION}.tar.gz
)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/flex/${REZ_BUILD_PROJECT_VERSION})

# We configure/build/install flex through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_FLEX
    URL ${FLEX_URL}
    PREFIX flex
    SOURCE_DIR ${EXTRACT_DIR}
    PATCH_COMMAND ""
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND bash ${CMAKE_SOURCE_DIR}/configure.sh ${EXTRACT_DIR}
    BUILD_COMMAND bash ${CMAKE_SOURCE_DIR}/build.sh ${EXTRACT_DIR}
    INSTALL_COMMAND bash ${CMAKE_SOURCE_DIR}/install.sh ${EXTRACT_DIR}
)

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] flex-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
