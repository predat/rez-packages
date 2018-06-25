CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url )

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=on)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

# Create a wrapper script for configure commands
set(DEP_ROOT ${PROJECT_BINARY_DIR}/DEPENDENCIES_PREFIX)
set(PATH "${DEP_ROOT}/bin:$ENV{PATH}")


#ExternalProject_add(
#    gafferDependencies
#    #URL https://github.com/GafferHQ/dependencies/releases/download/0.47.0.0/gafferDependencies-0.47.0.0-linux.tar.gz
#    URL /users/smaziere/Downloads/gafferDependencies-0.47.0.0-linux.tar.gz
#    PREFIX gafferDependencies
#    UPDATE_COMMAND ""
#    CONFIGURE_COMMAND ""
#    BUILD_COMMAND ""
#    BUILD_IN_SOURCE 1
#    INSTALL_COMMAND  sh -c "cp -ar ${CMAKE_BINARY_DIR}/gafferDependencies/src/gafferDependencies/* ${CMAKE_INSTALL_PREFIX}"
#)


ExternalProject_add(
    gaffer
    #DEPENDS gafferDependencies
    PREFIX gaffer
    GIT_REPOSITORY https://github.com/GafferHQ/gaffer.git
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND scons -j 8 BUILD_DIR=${CMAKE_INSTALL_PREFIX} INSTALL_DIR=${CMAKE_INSTALL_PREFIX} build
    BUILD_IN_SOURCE 1
    INSTALL_COMMAND ""
)

