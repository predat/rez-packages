CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(version ${REZ_BUILD_PACKAGE_VERSION})
set(pkg_name ${REZ_BUILD_PACKAGE_NAME})
set(url https://github.com/yaml/libyaml/archive/0.2.2.tar.gz)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    libYaml
    URL ${url}
    PREFIX libYaml
    UPDATE_COMMAND ./bootstrap
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --enable-static --enable-shared
    INSTALL_COMMAND "${install_cmd}"
    # ALWAYS 1
    BUILD_IN_SOURCE 1
)

install(CODE "message(STATUS Running Phony install)")

# install(
#     FILES cmake/libyaml.cmake
#     DESTINATION cmake
# )
