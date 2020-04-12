CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)

rez_find_packages(PREFIX pkgs AUTO)


set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version ${REZ_BUILD_PROJECT_VERSION})
set(url https://www.nasm.us/pub/${name}/releasebuilds/${version}/${name}-${version}.tar.xz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make -j ${ncpu} install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND ${install_cmd}
    BUILD_COMMAND $(MAKE) -j${ncpus}
    BUILD_IN_SOURCE 1
)


INSTALL(CODE "message(STATUS Running Phony install)")
