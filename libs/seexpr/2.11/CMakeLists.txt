CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


rez_find_packages(PREFIX pkgs AUTO)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/wdas/SeExpr.git)
#set(tag v${version})
set(tag v2.11)
#set(tag db9610a24401fa7198c54c8768d0484175f54172)


if(${REZ_BUILD_INSTALL})
    set(install_cmd VERBOSE=1 make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    #URL ${url}
    GIT_REPOSITORY ${url}
    GIT_TAG ${tag}
    PREFIX ${name}
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DBUILD_DEMOS=OFF
    -DBUILD_DOC=OFF
    -DBUILD_TESTS=OFF
    -DBUILD_UTILS=OFF
    -DBOOST_DIR=$ENV{REZ_BOOST_ROOT}
    -DLLVM_DIR=$ENV{REZ_LLVM_ROOT}
    -DPYQT_SIP_DIR=$ENV{REZ_PYQT4_ROOT}/share/sip
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON
    INSTALL_COMMAND "${install_cmd}"
)
