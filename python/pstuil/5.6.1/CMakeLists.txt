CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezPipInstall)

set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url https://github.com/giampaolo/psutil/archive/release-5.6.1.tar.gz)

rez_pip_install(
    psutil
    URL ${url}
)

install(CODE "message(STATUS Running Phony install)")

