CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/${name}/${name}/archive/${version}.tar.gz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make GLEW_DEST="${CMAKE_INSTALL_PREFIX}" -j$ENV{REZ_BUILD_THREAD_COUNT} install)
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DGLFW_BUILD_TESTS=OFF
    -DGLFW_BUILD_EXAMPLES=OFF
    -DGLFW_BUILD_DOCS=OFF
    -DCMAKE_BUILD_TYPE=Release
    -DBUILD_SHARED_LIBS=ON
)


ExternalProject_add(
    ${name}-static
    URL ${url}
    PREFIX ${name}-static
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DGLFW_BUILD_TESTS=OFF
    -DGLFW_BUILD_EXAMPLES=OFF
    -DGLFW_BUILD_DOCS=OFF
    -DCMAKE_BUILD_TYPE=Release
)

install(
    FILES cmake/glfw.cmake
    DESTINATION cmake
)
