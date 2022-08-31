cmake_minimum_required(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

execute_process(
    COMMAND
    bash ""
    RESULT_VARIABLE RETURN_CODE
)

# We check that the execute_process() macro terminated properly.
# If not, we abort the process.
if(RETURN_CODE EQUAL "1")
    message(FATAL_ERROR "[CMAKE] Install script returned an error code. Aborting...")
endif()


# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
		COMMAND echo \"\n[CMAKE] VFX Reference Platform 2023 PACKAGE SETUP FINISHED!\n\"
    )"
)
