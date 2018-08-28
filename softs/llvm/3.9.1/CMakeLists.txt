# Found here: https://github.com/seahorn/seatooling/blob/master/CMakeLists.txt
#

cmake_minimum_required(VERSION 2.8.12)
include(RezBuild)
include(RezRepository)
include(ExternalProject)


find_package(Git REQUIRED)


option (WITH_CLANG "Compile LLVM with Clang" ON)


set (TAG "release_39" CACHE STRING "LLVM tag")
set (git_url https://git.llvm.org/git)


add_custom_target (llvm-src
    # HACK: remove all sources so that git-clone does not fail
    # HACK: a proper solution is to work arround this as in ExternalProject
    ${CMAKE_COMMAND} -E remove_directory ${CMAKE_CURRENT_BINARY_DIR}/ext/llvm
    COMMAND
    ${GIT_EXECUTABLE} clone --depth=1 --branch=${TAG}
    ${git_url}/llvm.git ${CMAKE_CURRENT_BINARY_DIR}/ext/llvm
)

if (WITH_CLANG)
  add_custom_target (clang-src
    ${GIT_EXECUTABLE} clone --depth=1 --branch=${TAG}
    ${git_url}/clang.git
    ${CMAKE_CURRENT_BINARY_DIR}/ext/llvm/tools/clang
    DEPENDS llvm-src)
  add_custom_target (compiler-rt
    ${GIT_EXECUTABLE} clone --depth=1 --branch=${TAG}
    ${git_url}/compiler-rt.git
    ${CMAKE_CURRENT_BINARY_DIR}/ext/llvm/projects/compiler-rt
    DEPENDS clang-src)
  add_custom_target (openmp
    ${GIT_EXECUTABLE} clone --depth=1 --branch=${TAG}
    ${git_url}/openmp.git
    ${CMAKE_CURRENT_BINARY_DIR}/ext/llvm/projects/openmp
    DEPENDS clang-src)
endif()


if (WITH_CLANG)
  set (LAST_LLVM_SRC openmp)
else()
  set (LAST_LLVM_SRC llvm-src)
endif()


add_custom_target (download-llvm-src DEPENDS ${LAST_LLVM_SRC})


set_property(DIRECTORY PROPERTY EP_STEP_TARGETS configure build test)
# build llvm using previously downloaded source
ExternalProject_Add (llvm
    DEPENDS download-llvm-src
    DOWNLOAD_COMMAND ""
    SOURCE_DIR ${CMAKE_CURRENT_BINARY_DIR}/ext/llvm
    #INSTALL_DIR ${CMAKE_BINARY_DIR}/run
    INSTALL_DIR ${CMAKE_INSTALL_PREFIX}
    CMAKE_ARGS
    -DCMAKE_C_COMPILER=${CMAKE_C_COMPILER} -DCMAKE_CXX_COMPILER=${CMAKE_CXX_COMPILER}
    -DCMAKE_BUILD_TYPE:STRING=${CMAKE_BUILD_TYPE}
    -DCMAKE_INSTALL_PREFIX:PATH=<INSTALL_DIR>
    -DLLVM_TARGETS_TO_BUILD:STRING=X86
    -DLLVM_ENABLE_PEDANTIC=OFF
    -DLLVM_ENABLE_PIC=ON
    -DLLVM_REQUIRES_RTTI:BOOL=TRUE
    -DLLVM_BUILD_LLVM_DYLIB:BOOL=TRUE
)
