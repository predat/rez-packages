CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(blender_version $ENV{REZ_BUILD_PROJECT_VERSION})

#rez_set_archive(
#    url_blender blender/blender-${blender_version}.tar.gz
#    https://github.com/glfw/glfw/archive/${glfw_version}.tar.gz
#)

set(url_blender
    https://ftp.nluug.nl/pub/graphics/blender/release/Blender2.79/blender-2.79b-linux-glibc219-x86_64.tar.bz2)

set(install_cmd ${CMAKE_CURRENT_SOURCE_DIR}/install.sh
    ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX})


ExternalProject_add(
    blender
    URL ${url_blender}
    PREFIX blender
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND "${install_cmd}"
)
