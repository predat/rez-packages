cmake_minimum_required(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(GMP_VERSION 6.1.0)
set(MPFR_VERSION 3.1.4)
set(MPC_VERSION 1.0.3)
set(ISL_VERSION 0.18)

# GCC
# It should be noted that trying to build GCC < 7.2 with glibc > 2.26 will generate two types of compilation errors,
# that can be alleviated by applying some patches to the code inside the GCC archive that will be used.
# As such, the burden of patching GCC is on the user, and not this script, at least for now.
# The patches can be found at the following links:
# * https://github.com/easybuilders/easybuild-easyconfigs/blob/master/easybuild/easyconfigs/g/GCCcore/GCCcore-6.3.0_fix-linux-unwind-fix-ucontext.patch
# * https://github.com/easybuilders/easybuild-easyconfigs/blob/master/easybuild/easyconfigs/g/GCCcore/GCCcore-6.3.0_fix-sanitizer_linux.patch
rez_set_archive(
    GCC_URL gcc/gcc-${REZ_BUILD_PROJECT_VERSION}.tar.xz
		https://ftp.gnu.org/gnu/gcc/gcc-9.3.0/${REZ_BUILD_PROJECT_VERSION}.tar.xz
    # Or https://ftp.gnu.org/gnu/gcc/gcc-${REZ_BUILD_PROJECT_VERSION}/gcc-${REZ_BUILD_PROJECT_VERSION}.tar.bz2 is we want to use 6.3.0 instead for example, since 6.3.1 is not directly available to download as we have to extract it from the EL7 devtoolset.
)
# GMP
rez_set_archive(
    gmp_url gmp/gmp-${GMP_VERSION}.tar.bz2
    ftp://gcc.gnu.org/pub/gcc/infrastructure/gmp-${GMP_VERSION}.tar.bz2
)
# MPFR
rez_set_archive(
    mpfr_url mpfr/mpfr-${MPFR_VERSION}.tar.bz2
    ftp://gcc.gnu.org/pub/gcc/infrastructure/mpfr-${MPFR_VERSION}.tar.bz2
)
# MPC
rez_set_archive(
    mpc_url mpc/mpc-${MPC_VERSION}.tar.gz
    ftp://gcc.gnu.org/pub/gcc/infrastructure/mpc-${MPC_VERSION}.tar.gz
)
# ISL
rez_set_archive(
    isl_url isl/isl-${ISL_VERSION}.tar.bz2
    ftp://gcc.gnu.org/pub/gcc/infrastructure/isl-${ISL_VERSION}.tar.bz2
)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/gcc/${REZ_BUILD_PROJECT_VERSION})
set(BUILD_DIR ${EXTRACT_DIR}/build/objdir)

# We configure/build/install GCC through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_GCC
    URL ${GCC_URL}
    PREFIX gcc
    SOURCE_DIR ${EXTRACT_DIR}
    PATCH_COMMAND ""
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND bash ${CMAKE_SOURCE_DIR}/configure.sh ${CMAKE_SOURCE_DIR}/960-fix-ubsan-defref.patch ${EXTRACT_DIR} ${BUILD_DIR} ${GMP_VERSION} ${MPFR_VERSION} ${MPC_VERSION} ${ISL_VERSION}
    BUILD_COMMAND bash ${CMAKE_SOURCE_DIR}/build.sh ${BUILD_DIR}
    INSTALL_COMMAND bash ${CMAKE_SOURCE_DIR}/install.sh ${BUILD_DIR}
)

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] GCC-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
