CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezPipInstall)

set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url_pyseq "https://github.com/rsgalloway/pyseq/archive/${version}.tar.gz")

rez_pip_install(
    pyseq
    URL ${url_pyseq}
)

install(CODE "message(STATUS Running Phony install)")

