#!/bin/bash

TMPDIR="/datas/tmp"
VERSION="${REZ_BUILD_PROJECT_VERSION}"
NAME="${REZ_BUILD_PROJECT_NAME}"

BASE_URL="https://github.com/${NAME}/llvm-project/releases/download/llvmorg-${VERSION}"
ARCHIVE="${NAME}-project-${VERSION}.src"
EXT='tar.xz'

#
# LLVM
#
if [[ ! -f ${TMPDIR}/${ARCHIVE}.${EXT} ]];then
    echo -n "**** Downloading ${ARCHIVE}.${EXT}... "
    curl -L -s -o "${TMPDIR}/${ARCHIVE}.${EXT}" "${BASE_URL}/${ARCHIVE}.${EXT}"
    echo "done"
else
    echo "**** Skip download file $TMPDIR/$ARCHIVE already exists."
fi

if [[ ! -d "${ARCHIVE}" ]]; then
    echo -n "**** Extract archive..."
    XZ_DEFAULTS="-T0" XZ_OPT="-2 -T0" tar -xf "${TMPDIR}/${ARCHIVE}.${EXT}"
    echo "done"
fi

cd "${ARCHIVE}"

#
# Building
#

mkdir -v build &&
cd       build &&

#CC=clang CXX=clang++                                   \
# cmake -DCMAKE_INSTALL_PREFIX=${REZ_BUILD_INSTALL_PATH} \
#       -DCMAKE_BUILD_TYPE=Release                       \
#       -DLLVM_ENABLE_RTTI=ON                            \
#       -DLLVM_TARGETS_TO_BUILD="host"                   \
#       -DLLVM_BUILD_TESTS=OFF                           \
#       -DLLVM_BUILD_EXAMPLES=OFF                        \
#       -DLLVM_ENABLE_LIBCXX=ON                          \
#       -DLLVM_ENABLE_FFI=ON                             \
#       -DLLVM_BUILD_LLVM_DYLIB=ON                       \
#       -DLLVM_LINK_LLVM_DYLIB=ON                        \
#       #-DLLVM_ENABLE_PROJECTS="clang;libcxx;libcxxabi;lldb"  \
#       -DSWIG_DIR=${REZ_SWIG_ROOT}/bin                  \
#       -DSWIG_EXECUTABLE=${REZ_SWIG_ROOT}/bin/swig      \
#       -DLLDB_TEST_C_COMPILER=gcc                       \
#       -DLLDB_TEST_CXX_COMPILER=g++                     \
#       -Wno-dev -G Ninja ../llvm
#make -j12
#make install

echo "**** Configure llvm build"
cmake -DCMAKE_INSTALL_PREFIX=${REZ_BUILD_INSTALL_PATH}                     \
      -DCMAKE_BUILD_TYPE=Release                                           \
      -DLLVM_BUILD_TESTS=OFF                                               \
      -DLLVM_BUILD_EXAMPLES=OFF                                            \
      -DLLVM_ENABLE_PROJECTS="clang;clang-tools-extra;llvm;lld;lldb"  \
      -DLLVM_ENABLE_RUNTIMES="all"                                         \
      -DLLVM_ENABLE_RTTI=ON                            \
      -DLLVM_ENABLE_FFI=ON                             \
      -DSWIG_DIR=${REZ_SWIG_ROOT}/bin                                      \
      -DSWIG_EXECUTABLE=${REZ_SWIG_ROOT}/bin/swig                          \
      -DLLDB_TEST_C_COMPILER=gcc                                           \
      -DLLDB_TEST_CXX_COMPILER=g++                                         \
      -Wno-dev -G Ninja ../llvm

echo "Building llvm... "
ninja

echo "Install llvm..."
ninja install


