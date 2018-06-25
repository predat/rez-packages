CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(blender_version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url_blender https://ftp.nluug.nl/pub/graphics/blender/release/Blender2.79/blender-2.79b-linux-glibc219-x86_64.tar.bz2)


ExternalProject_add(
    ${name}
    URL ${url_blender}
    PREFIX ${name}
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ""
)

install(
   DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/${name}/src/${name}/
   DESTINATION ${CMAKE_INSTALL_PREFIX}
   USE_SOURCE_PERMISSIONS
)
