CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)

# We split the PySide2 version string in multiple ones.
string(REPLACE "." ";" PYSIDE_VERSION_LIST ${REZ_BUILD_PROJECT_VERSION})
list(GET PYSIDE_VERSION_LIST 0 PYSIDE_VERSION_MAJOR)
list(GET PYSIDE_VERSION_LIST 1 PYSIDE_VERSION_MINOR)
list(GET PYSIDE_VERSION_LIST 2 PYSIDE_VERSION_PATCH)
list(GET PYSIDE_VERSION_LIST 3 PYSIDE_VERSION_PYTHON)

# We create Pythonless version of PySide2 to make it match with the one in the archive name.
set(PYSIDE_PYTHONLESS_VERSION "${PYSIDE_VERSION_MAJOR}.${PYSIDE_VERSION_MINOR}.${PYSIDE_VERSION_PATCH}")

# PySide2
rez_set_archive(
    # This is a relative path from the ${REZ_REPO_PAYLOAD_DIR} environment variable,
    # that is pointing to the root directory where we can find all the archives of the package
    # we can build, using the following hierarchy:
    # "${REZ_REPO_PAYLOAD_DIR}/project_name/archive.what.ever"
    PYSIDE_URL pyside2/PySide2-${PYSIDE_PYTHONLESS_VERSION}-${PYSIDE_PYTHONLESS_VERSION}-cp27-cp27mu-manylinux1_x86_64.whl
    https://download.qt.io/official_releases/QtForPython/pyside2/PySide2-${PYSIDE_PYTHONLESS_VERSION}-${PYSIDE_PYTHONLESS_VERSION}-cp27-cp27mu-manylinux1_x86_64.whl
)

# In the case of a Python pip wheel file, we do not have any archive to extract, so we can just execute our Bash
# script(s) inside an "execute_process" macro.
execute_process(
    COMMAND
    bash ${CMAKE_SOURCE_DIR}/install.sh ${PYSIDE_URL}
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
        COMMAND echo \"\n[CMAKE] Pyside2-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
