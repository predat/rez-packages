CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(blender_version $ENV{REZ_BUILD_PROJECT_VERSION})

#rez_set_archive(
#    url_blender blender/blender-${blender_version}.tar.gz
#    https://github.com/glfw/glfw/archive/${glfw_version}.tar.gz
#)

set(url_pkg https://github.com/appleseedhq/appleseed/releases/download/1.9.0-beta/appleseed-1.9.0-beta-0-g5693918-linux64-gcc48.zip)

set(install_cmd ${CMAKE_CURRENT_SOURCE_DIR}/install.sh
    ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX})


ExternalProject_add(
    appleseed
    URL ${url_pkg}
    PREFIX appleseed
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND "${install_cmd}"
)
