CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# We configure/build/install numpy through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.

execute_process(
    COMMAND
    bash ${CMAKE_SOURCE_DIR}/install.sh ${REZ_BUILD_PROJECT_VERSION}
    RESULT_VARIABLE RETURN_CODE
)

# We check that the execute_process() macro terminated properly.
# If not, we abort the process.
if(RETURN_CODE EQUAL "1")
    message(FATAL_ERROR "[CMAKE] Install script returned an error code. Aborting...")
endif()

# ExternalProject_Add(
    # REZ_NUMPY
    # PREFIX numpy
    # SOURCE_DIR "./"
    # PATCH_COMMAND ""
    # UPDATE_COMMAND ""
    # CONFIGURE_COMMAND ""
    # BUILD_COMMAND ""
    # INSTALL_COMMAND bash ${CMAKE_SOURCE_DIR}/install.sh ${REZ_BUILD_PROJECT_VERSION}
# )

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] NumPy-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
