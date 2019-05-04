CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(ExternalProject)


if(${MAYA_MAJOR_VERSION} EQUAL 2015)
    set(arch_maya "")
    set(ADLM_RELEASE R9)
elseif(${MAYA_MAJOR_VERSION} EQUAL 2016)
    set(arch_maya "_64bit")
    set(ADLM_RELEASE R11)
elseif(${MAYA_MAJOR_VERSION} EQUAL 2018)
    set(arch_maya "_64bit")
    set(ADLM_RELEASE R14)
else()
    set(arch_maya "_64bit")
    set(ADLM_RELEASE R12)
endif()


set(syncfg_file Maya${MAYA_MAJOR_VERSION}.${MAYA_MAJOR_VERSION}.${MAYA_PATCH_VERSION}.64.syncfg)
set(MAYA_EXECUTABLE ${CMAKE_INSTALL_PREFIX}/maya/bin/maya.bin)  # use in config/synergy.syncfg.in
set(MAYA_WRAPPER ${CMAKE_INSTALL_PREFIX}/maya/bin/maya${MAYA_MAJOR_VERSION})  # use in config/synergy.syncfg.in
set(url http://up.autodesk.com/${MAYA_MAJOR_VERSION}/MAYA/305DF702-6C4B-4765-9E8B-EE90539F611C/Autodesk_Maya_${MAYA_MAJOR_VERSION}_${MAYA_PATCH_VERSION}_Update_Linux${arch_maya}.tgz)
set(build_cmd ${CMAKE_CURRENT_SOURCE_DIR}/extract.sh  ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR} ${MAYA_MAJOR_VERSION} )


configure_file(config/synergy.syncfg.in ${syncfg_file} @ONLY)
configure_file(config/AdlmThinClientCustomEnv.xml.in AdlmThinClientCustomEnv.xml @ONLY)
configure_file(config/License.env.in License.env @ONLY)
configure_file(config/bin/maya.in bin/maya @ONLY)
configure_file(config/bin/register_maya.in bin/register_maya @ONLY)


if(${REZ_BUILD_INSTALL})
    set(install_cmd ${CMAKE_CURRENT_SOURCE_DIR}/install.sh  ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX} ${MAYA_MAJOR_VERSION})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    maya
    URL ${url}
    URL_MD5 3569c929f05daf0b6a07593946eb1b1d
    PREFIX maya
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ${build_cmd}
    INSTALL_COMMAND ${install_cmd}
    BUILD_IN_SOURCE 0
)


rez_install_files(
    ${CMAKE_CURRENT_BINARY_DIR}/AdlmThinClientCustomEnv.xml
    ${CMAKE_CURRENT_BINARY_DIR}/${syncfg_file}
    RELATIVE build/platform-linux/arch-x86_64
    DESTINATION .
)

rez_install_files(
    config/MayaNoColorManagement.xml
    RELATIVE config
    DESTINATION .
)

rez_install_files(
    ${CMAKE_CURRENT_BINARY_DIR}/License.env
    RELATIVE build/platform-linux/arch-x86_64
    DESTINATION maya/bin
)

rez_install_files(
    config/license.lic
    RELATIVE config
    DESTINATION .
)

install(PROGRAMS
    ${CMAKE_CURRENT_BINARY_DIR}/bin/maya
    ${CMAKE_CURRENT_BINARY_DIR}/bin/register_maya
    DESTINATION maya/bin
)

rez_install_files(
    cmake/maya.cmake
    DESTINATION .
)
