CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(url_maxwell_studio https://software.nextlimit.com/authdl/_dYssh5IawkJ6YaUqemLvpXaVYBUvV0hgM/maxwell_studio_${MAXWELL_VERSION}_linux64.tar.gz)
set(url_maxwell_render https://software.nextlimit.com/authdl/_dSHFMAeW0FSS1oS7I6sRojQoBmTM1CA02/maxwell_render_${MAXWELL_VERSION}_linux64.tar.gz)

set(install_cmd ${CMAKE_CURRENT_SOURCE_DIR}/install.sh
    ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX} ${MAXWELL_VERSION})


ExternalProject_add(
    maxwell_studio
    URL ${url_maxwell_studio}
    PREFIX maxwell
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ${install_cmd} maxwell_studio
    BUILD_IN_SOURCE 1
)

ExternalProject_add(
    maxwell_render
    URL ${url_maxwell_render}
    PREFIX maxwell
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ${install_cmd} maxwell_render
    BUILD_IN_SOURCE 1
)
