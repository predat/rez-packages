#!/usr/bin/bash

# Will exit the Bash script the moment any command will itself exit with a non-zero status, thus an error.
set -e

EXTRACT_PATH=$1
BUILD_PATH=$2
INSTALL_PATH=${REZ_BUILD_INSTALL_PATH}
ALEMBIC_VERSION=${REZ_BUILD_PROJECT_VERSION}

# We print the arguments passed to the Bash script.
echo -e "\n"
echo -e "================="
echo -e "=== CONFIGURE ==="
echo -e "================="
echo -e "\n"

echo -e "[CONFIGURE][ARGS] EXTRACT PATH: ${EXTRACT_PATH}"
echo -e "[CONFIGURE][ARGS] BUILD PATH: ${BUILD_PATH}"
echo -e "[CONFIGURE][ARGS] INSTALL PATH: ${INSTALL_PATH}"
echo -e "[CONFIGURE][ARGS] ALEMBIC VERSION: ${ALEMBIC_VERSION}"

# We check if the arguments variables we need are correctly set.
# If not, we abort the process.
if [[ -z ${EXTRACT_PATH} || -z ${BUILD_PATH} || -z ${INSTALL_PATH} || -z ${ALEMBIC_VERSION} ]]; then
    echo -e "\n"
    echo -e "[CONFIGURE][ARGS] One or more of the argument variables are empty. Aborting..."
    echo -e "\n"

    exit 1
fi

# We run the configuration script of Alembic.
echo -e "\n"
echo -e "[CONFIGURE] Running the configuration script from Alembic-${ALEMBIC_VERSION}..."
echo -e "\n"

mkdir -p ${BUILD_PATH}
cd ${BUILD_PATH}

cmake \
    ${BUILD_PATH}/.. \
    -DCMAKE_INSTALL_PREFIX=${INSTALL_PATH} \
    -DCMAKE_C_FLAGS="-fPIC" \
    -DCMAKE_CXX_FLAGS="-fPIC" \
    -DALEMBIC_ILMBASE_LINK_STATIC=OFF \
    -DALEMBIC_LIB_USES_BOOST=OFF \
    -DALEMBIC_LIB_USES_TR1=OFF \
    -DALEMBIC_SHARED_LIBS=ON \
    -DUSE_ARNOLD=OFF \
    -DUSE_BINARIES=ON \
    -DUSE_EXAMPLES=OFF \
    -DUSE_HDF5=OFF \
    -DUSE_MAYA=OFF \
    -DUSE_PRMAN=OFF \
    -DUSE_PYALEMBIC=OFF \
    -DUSE_STATIC_BOOST=OFF \
    -DUSE_STATIC_HDF5=OFF \
    -DUSE_TESTS=OFF \
    -DBOOST_ROOT=${REZ_BOOST_ROOT} \
    -DIMATH_ROOT=${REZ_ILMBASE_ROOT} \

echo -e "\n"
echo -e "[CONFIGURE] Finished configuring Alembic-${ALEMBIC_VERSION}!"
echo -e "\n"
