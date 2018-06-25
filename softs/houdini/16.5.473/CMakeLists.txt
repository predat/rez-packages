CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(ExternalProject)


set(url_houdini ${CMAKE_CURRENT_SOURCE_DIR}/archives/houdini-${HOUDINI_VERSION}-$ENV{REZ_PLATFORM_VERSION}_$ENV{REZ_ARCH_VERSION}_gcc4.8.tar.gz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd ${CMAKE_CURRENT_SOURCE_DIR}/install.sh ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX} ${HOUDINI_VERSION})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    houdini
    URL ${url_houdini}
    # URL_MD5 ee00598d1f554bd9a6016956458f9b88
    # URL_MD5 8fa501a5d5d80635ee6f05c760f81af8 # qt4 version
    PREFIX houdini
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ${install_cmd}
    BUILD_IN_SOURCE 0
)
