#! /bin/bash

mkdir -p ${REZ_REPO_PAYLOAD_DIR}/gcc
wget -O ${REZ_REPO_PAYLOAD_DIR}/gcc/gcc-9.3.0.tar.xz https://ftp.gnu.org/gnu/gcc/gcc-9.3.0/gcc-9.3.0.tar.xz

mkdir -p ${REZ_REPO_PAYLOAD_DIR}/gmp
wget -O ${REZ_REPO_PAYLOAD_DIR}/gmp/gmp-6.1.0.tar.bz2 ftp://gcc.gnu.org/pub/gcc/infrastructure/gmp-6.1.0.tar.bz2

mkdir -p ${REZ_REPO_PAYLOAD_DIR}/mpfr
wget -O ${REZ_REPO_PAYLOAD_DIR}/mpfr/mpfr-3.1.4.tar.bz2 ftp://gcc.gnu.org/pub/gcc/infrastructure/mpfr-3.1.4.tar.bz2

mkdir -p ${REZ_REPO_PAYLOAD_DIR}/mpc
wget -O ${REZ_REPO_PAYLOAD_DIR}/mpc/mpc-1.0.3.tar.gz ftp://gcc.gnu.org/pub/gcc/infrastructure/mpc-1.0.3.tar.gz

mkdir -p ${REZ_REPO_PAYLOAD_DIR}/isl
wget -O ${REZ_REPO_PAYLOAD_DIR}/isl/isl-0.18.tar.bz2 ftp://gcc.gnu.org/pub/gcc/infrastructure/isl-0.18.tar.bz2

