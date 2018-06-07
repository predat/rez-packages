CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(RezRepository)
include(ExternalProject)


if(${REZ_BUILD_INSTALL})
    set(install_cmd ${CMAKE_CURRENT_SOURCE_DIR}/install.sh ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX} ${HOUDINI_VERSION})
else()
    set(install_cmd "")
endif()



ExternalProject_add(
    $ENV{REZ_BUILD_PROJECT_NAME}
    GIT_REPOSITORY git@git.prs.vfx.int:pipeline3.0/shotgun/apps/pptk-maya-musterManager.git
    #GIT_TAG $ENV{REZ_BUILD_PROJECT_VERSION}
    PREFIX $ENV{REZ_BUILD_PROJECT_NAME}
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND "${install_cmd}"
)
