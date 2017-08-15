CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)

#FILE(GLOB_RECURSE python_libs "install_deps/python/lib")
#rez_install_files(
#  ${python_libs}
#  DESTINATION .
#)

FILE(GLOB_RECURSE scripts "install_deps/scripts/*.sh")
rez_install_files(
  ${scripts}
  RELATIVE install_deps/scripts
  DESTINATION scripts
  EXECUTABLE
)

include(RezPipInstall)
set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url "$ENV{REZ_REPO_PAYLOAD_DIR}/PyOpenGL/PyOpenGL-${version}.tar.gz")

rez_pip_install(
    PyOpenGL
    URL ${url}
)
