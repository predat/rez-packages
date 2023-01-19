cmake_minimum_required(VERSION 2.8.12)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url https://download.qt.io/development_releases/prebuilt/libclang/libclang-release_140-based-linux-Rhel8.2-gcc9.2-x86_64.7z)


# get_cmake_property(_variableNames VARIABLES)
# list (SORT _variableNames)
# foreach (_variableName ${_variableNames})
#     message(STATUS "${_variableName}=${${_variableName}}")
# endforeach()


ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    BUILD_IN_SOURCE 1
    INSTALL_COMMAND ${CMAKE_COMMAND} -E copy_directory $ENV{PWD}/llvm/src/llvm
    $ENV{REZ_BUILD_INSTALL_PATH}/

)


INSTALL(CODE "message(STATUS Running Phony install)")
