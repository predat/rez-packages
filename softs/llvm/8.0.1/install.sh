#!/bin/bash

TMP_DIR="/tmp"
VERSION="${REZ_BUILD_PROJECT_VERSION}"
NAME="${REZ_BUILD_PROJECT_NAME}"
BASE_URL="https://github.com/${NAME}/llvm-project/releases/download/llvmorg-${VERSION}"
ARCHIVE="${NAME}-${VERSION}.src"
EXT='tar.xz'


#
# LLVM
#
if [[ ! -f ${TMP_DIR}/${ARCHIVE}.${EXT} ]];then
    echo -n "Downloading ${ARCHIVE}.${EXT}... "
    curl -L -s -o "${TMP_DIR}/${ARCHIVE}.${EXT}" "${BASE_URL}/${ARCHIVE}.${EXT}"
    echo "done"
fi

tar -xf "${TMP_DIR}/${ARCHIVE}.${EXT}"
cd "${ARCHIVE}"


for pkg in {cfe,compiler-rt,openmp,libcxx,libcxxabi,lld,lldb}
do
    if [[ ! -f ${TMP_DIR}/${pkg}-${VERSION}.src.${EXT} ]]; then
        echo -n "Downloading ${pkg}-${VERSION}.src.${EXT}... "
        curl -L -s -o "${TMP_DIR}/${pkg}-${VERSION}.src.${EXT}" "${BASE_URL}/${pkg}-${VERSION}.src.${EXT}"
        echo "done"
    fi
done

#
# clang
#
echo -n "Extracting clang source... "
tar -xf "${TMP_DIR}/cfe-${VERSION}.src.tar.xz" -C tools
mv "tools/cfe-${VERSION}.src" tools/clang
echo "done"

#
# lld
#
echo -n "Extracting lld source... "
tar -xf "${TMP_DIR}/lld-${VERSION}.src.tar.xz" -C tools
mv "tools/lld-${VERSION}.src" tools/lld
echo "done"

#
# lldb
#
echo -n "Extracting lldb source... "
tar -xf "${TMP_DIR}/lldb-${VERSION}.src.tar.xz" -C tools
mv "tools/lldb-${VERSION}.src" tools/lldb
echo "done"


for pkg in {compiler-rt,openmp,libcxx,libcxxabi}
do
    echo -n "Extracting ${pkg}-${VERSION}.src.${EXT}... "
    tar -xf "${TMP_DIR}/${pkg}-${VERSION}.src.tar.xz" -C projects
    mv "projects/${pkg}-${VERSION}.src" "projects/${pkg}"
    echo "done"
done


#
# Building
#
echo -n "Building llvm... "
mkdir -v build &&
cd       build &&

#CC=clang CXX=clang++                                   \
cmake -DCMAKE_INSTALL_PREFIX=${REZ_BUILD_INSTALL_PATH} \
      -DCMAKE_BUILD_TYPE=Release                       \
      -DLLVM_ENABLE_RTTI:BOOL=ON                       \
      -DLLVM_TARGETS_TO_BUILD="host"                   \
      -DLLVM_BUILD_TESTS:BOOL=OFF                      \
      -DLLVM_BUILD_EXAMPLES:BOOL=OFF                   \
      -DLLVM_ENABLE_LIBCXX:BOOL=ON                     \
      -DLLVM_ENABLE_FFI=ON                             \
      -DLLVM_BUILD_LLVM_DYLIB=ON                       \
      -DLLVM_LINK_LLVM_DYLIB=ON                        \
      -DSWIG_DIR=${REZ_SWIG_ROOT}/bin                  \
      -DSWIG_EXECUTABLE=${REZ_SWIG_ROOT}/bin/swig      \
      -DLLDB_TEST_C_COMPILER=gcc                       \
      -DLLDB_TEST_CXX_COMPILER=g++                     \
      -Wno-dev -G Ninja ..


ninja
ninja install
