CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(blenderseed_version $ENV{REZ_BUILD_PROJECT_VERSION})

#rez_set_archive(
#    url_blender blender/blender-${blender_version}.tar.gz
#    https://github.com/glfw/glfw/archive/${glfw_version}.tar.gz
#)

set(url_pkg
    https://github.com/appleseedhq/blenderseed/releases/download/0.8.1-beta/blenderseed-0.8.1-beta.zip)

set(install_cmd ${CMAKE_CURRENT_SOURCE_DIR}/install.sh
    ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX})


ExternalProject_add(
    blenderseed
    URL ${url_pkg}
    PREFIX blenderseed
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND "${install_cmd}"
)
