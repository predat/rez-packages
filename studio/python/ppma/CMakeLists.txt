CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(stagingpath "${CMAKE_BINARY_DIR}/staging")
set(destpath "${stagingpath}/python")
set(destbinpath "${stagingpath}/bin")
set(destincpath "${stagingpath}/include")
set(destdatapath "${stagingpath}")


if(${REZ_BUILD_INSTALL})
    set(install_cmd ${CMAKE_COMMAND} -E copy_directory ${stagingpath} ${CMAKE_INSTALL_PREFIX} )
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    $ENV{REZ_BUILD_PROJECT_NAME}
    GIT_REPOSITORY git@git.prs.vfx.int:pipeline3.0/python/$ENV{REZ_BUILD_PROJECT_NAME}.git
    GIT_TAG $ENV{REZ_BUILD_PROJECT_VERSION}
    PREFIX $ENV{REZ_BUILD_PROJECT_NAME}
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND
        COMMAND pip install ${pipargs} --no-deps
        --install-option=--install-scripts=${CMAKE_INSTALL_PREFIX}/bin
        --install-option=--install-lib=${CMAKE_INSTALL_PREFIX}/python
        --install-option=--install-headers=${CMAKE_INSTALL_PREFIX}/python
        --install-option=--install-data=${CMAKE_INSTALL_PREFIX} .
)

FILE(GLOB_RECURSE userSetup "install_deps/python/userSetup.py")
rez_install_files(
    ${userSetup}
    RELATIVE install_deps/python
    DESTINATION setup
)

rez_install_files(
    "install_deps/menu/ppMenu.yml"
    RELATIVE install_deps/menu
    DESTINATION common
)
