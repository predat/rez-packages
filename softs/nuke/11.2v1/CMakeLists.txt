CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(ExternalProject)


set(url_nuke ${CMAKE_CURRENT_SOURCE_DIR}/archives/Nuke11.2v1-linux-x86-release-64.tgz)
set(CUSTOM_VERSION ${NUKE_MAJOR_VERSION}.${NUKE_MINOR_VERSION}v${NUKE_PATCH_VERSION})
set(build_cmd ${CMAKE_CURRENT_SOURCE_DIR}/extract.sh ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR} ${CUSTOM_VERSION} )


configure_file(config/bin/nuke.in bin/nuke @ONLY)
configure_file(config/bin/nukex.in bin/nukex @ONLY)
configure_file(config/bin/nukestudio.in bin/nukestudio @ONLY)
configure_file(config/bin/nukeassist.in bin/nukeassist @ONLY)


if(${REZ_BUILD_INSTALL})
    set(install_cmd ${CMAKE_CURRENT_SOURCE_DIR}/install.sh
        ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX} ${CUSTOM_VERSION})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    nuke
    URL ${url_nuke}
    PREFIX nuke
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ${build_cmd}
    INSTALL_COMMAND ${install_cmd}
    BUILD_IN_SOURCE 1
)


install(PROGRAMS
    ${CMAKE_CURRENT_BINARY_DIR}/bin/nuke
    ${CMAKE_CURRENT_BINARY_DIR}/bin/nukeassist
    ${CMAKE_CURRENT_BINARY_DIR}/bin/nukex
    ${CMAKE_CURRENT_BINARY_DIR}/bin/nukestudio
    DESTINATION nuke
)


#rez_install_files(
#    cmake/maya.cmake
#    DESTINATION .
#)

