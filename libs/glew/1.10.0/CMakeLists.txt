CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(glew_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_glew glew/glew-${glew_version}.tgz
    https://sourceforge.net/projects/glew/files/glew/${glew_version}/glew-${glew_version}.tgz
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install GLEW_DEST=${CMAKE_INSTALL_PREFIX})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    glew
    URL ${url_glew}
    PREFIX glew
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j ${ncpus} GLEW_DEST=${CMAKE_INSTALL_PREFIX}
)
