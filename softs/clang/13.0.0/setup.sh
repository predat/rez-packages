#! /bin/bash

mkdir -p ${REZ_REPO_PAYLOAD_DIR}/llvm
wget -O ${REZ_REPO_PAYLOAD_DIR}/llvm/llvm-13.0.0.src.tar.xz https://github.com/llvm/llvm-project/archive/refs/tags/llvmorg-13.0.0.tar.gz
