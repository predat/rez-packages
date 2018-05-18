CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(ExternalProject)


set(url_pkg https://github.com/Psyop/Cryptomatte.git)


# if(${REZ_BUILD_INSTALL})
#     set(install_cmd make install ${make_args})
# else()
#     set(install_cmd "")
# endif()


# get_cmake_property(_variableNames VARIABLES)
# list (SORT _variableNames)
# foreach (_variableName ${_variableNames})
#     message(STATUS "${_variableName}=${${_variableName}}")
# endforeach()


ExternalProject_add(
    cryptomatte
    GIT_REPOSITORY ${url_pkg}
    GIT_TAG ${REZ_BUILD_PROJECT_VERSION}
    PREFIX cryptomatte
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ""
    #BUILD_IN_SOURCE 0
)


install(
    DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/cryptomatte/src/cryptomatte/nuke/
    DESTINATION ${CMAKE_INSTALL_PREFIX}/
)
