CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(RezPipInstall)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url_requests "https://github.com/${name}/${name}/archive/v${version}.tar.gz")


rez_pip_install(
    requests
    URL ${url_requests}
)
