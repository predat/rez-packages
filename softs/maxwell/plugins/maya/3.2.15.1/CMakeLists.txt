CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


#set(url_pkg https://software.nextlimit.com/authdl/_dLT5ybxPxurDZNMZjLUoDawYfCkmgyA0B/maxwell-maya-linux-4.2.1.zip)
set(url_pkg ${CMAKE_CURRENT_SOURCE_DIR}/archives/maxwell-maya-linux-3.2.15.zip)

set(install_cmd ${CMAKE_CURRENT_SOURCE_DIR}/install.sh
    ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX})

set(build_cmd ${CMAKE_CURRENT_SOURCE_DIR}/extract.sh
    ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX})


ExternalProject_add(
    $ENV{REZ_BUILD_PROJECT_NAME}
    URL ${url_pkg}
    URL_MD5 6d312e1d71538691951885337c88c33f
    PREFIX $ENV{REZ_BUILD_PROJECT_NAME}
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ${build_cmd}
    INSTALL_COMMAND ${install_cmd}
)
