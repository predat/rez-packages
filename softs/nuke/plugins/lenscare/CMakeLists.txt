CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(ExternalProject)


set(url_pkg "http://www.frischluft.com/download/lenscare_ofx_v1.44(linux).zip")


ExternalProject_add(
    lenscare
    URL ${url_pkg}
    PREFIX lenscare
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ""
)


install(
    DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/lenscare/src/lenscare/
    DESTINATION ${CMAKE_INSTALL_PREFIX}/
)

rez_install_files(
    config/lenscare_ofx_Fix_Studio.lic
    RELATIVE config
    DESTINATION .
)
