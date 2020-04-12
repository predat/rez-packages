CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)

rez_find_packages(PREFIX pkgs AUTO)


set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version ${REZ_BUILD_PROJECT_VERSION})
set(url https://netix.dl.sourceforge.net/project/${name}/${name}/${version}/${name}-${version}.tar.gz)



if(${REZ_BUILD_INSTALL})
    set(install_cmd make -j ${ncpu} install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    CMAKE_ARGS
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DFREEGLUT_BUILD_DEMOS=OFF
    -DCMAKE_INSTALL_LIBDIR=lib
)


INSTALL(CODE "message(STATUS Running Phony install)")
