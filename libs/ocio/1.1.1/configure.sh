#!/usr/bin/bash

# Will exit the Bash script the moment any command will itself exit with a non-zero status, thus an error.
set -e

EXTRACT_PATH=$1
BUILD_PATH=$2
INSTALL_PATH=${REZ_BUILD_INSTALL_PATH}
OCIO_VERSION=${REZ_BUILD_PROJECT_VERSION}

# We print the arguments passed to the Bash script.
echo -e "\n"
echo -e "================="
echo -e "=== CONFIGURE ==="
echo -e "================="
echo -e "\n"

echo -e "[CONFIGURE][ARGS] EXTRACT PATH: ${EXTRACT_PATH}"
echo -e "[CONFIGURE][ARGS] BUILD PATH: ${BUILD_PATH}"
echo -e "[CONFIGURE][ARGS] INSTALL PATH: ${INSTALL_PATH}"
echo -e "[CONFIGURE][ARGS] OCIO VERSION: ${OCIO_VERSION}"

# We check if the arguments variables we need are correctly set.
# If not, we abort the process.
if [[ -z ${EXTRACT_PATH} || -z ${BUILD_PATH} || -z ${INSTALL_PATH} || -z ${OCIO_VERSION} ]]; then
    echo -e "\n"
    echo -e "[CONFIGURE][ARGS] One or more of the argument variables are empty. Aborting..."
    echo -e "\n"

    exit 1
fi

# We run the configuration script of OCIO.
echo -e "\n"
echo -e "[CONFIGURE] Running the configuration script from OCIO-${OCIO_VERSION}..."
echo -e "\n"

mkdir -p ${BUILD_PATH}
cd ${BUILD_PATH}

# Necessary to disable the -Werror flag in order to build without issues on modern compilers.
sed "s|set(EXTERNAL_COMPILE_FLAGS \"\${EXTERNAL_COMPILE_FLAGS} -Werror\")||1" --in-place ${EXTRACT_PATH}/src/core/CMakeLists.txt
sed "s|set(CMAKE_CXX_FLAGS \"\${CMAKE_CXX_FLAGS} -Werror\")||1" --in-place ${EXTRACT_PATH}/src/pyglue/CMakeLists.txt

cmake \
    ${BUILD_PATH}/.. \
    -DCMAKE_INSTALL_PREFIX=${INSTALL_PATH} \
    -DCMAKE_C_FLAGS="-fPIC" \
    -DCMAKE_CXX_FLAGS="-fPIC -I${REZ_TINYXML_ROOT}/include" \
    -DCMAKE_POLICY_DEFAULT_CMP0072=NEW \
    -DCMAKE_POLICY_DEFAULT_CMP0074=NEW \
    -DOCIO_BUILD_APPS=OFF \
    -DOCIO_BUILD_DOCS=OFF \
    -DOCIO_BUILD_JNIGLUE=OFF \
    -DOCIO_BUILD_NUKE=OFF \
    -DOCIO_BUILD_PYGLUE=ON \
    -DOCIO_BUILD_TESTS=OFF \
    -DOCIO_BUILD_TRUELIGHT=OFF \
    -DOCIO_STATIC_JNIGLUE=OFF \
    -DOCIO_USE_BOOST_PTR=OFF \
    -DOCIO_USE_SSE=ON \
    -DUSE_EXTERNAL_LCMS=ON \
    -DUSE_EXTERNAL_TINYXML=ON \
    -DUSE_EXTERNAL_YAML=ON \
    -DBoost_NO_BOOST_CMAKE=ON \
    -DBoost_NO_SYSTEM_PATHS=ON \
    -DBOOST_ROOT=${REZ_BOOST_ROOT} \
    -DTINYXML_INCLUDE_DIR=${REZ_TINYXML_ROOT}/include \
    -DTINYXML_LIBRARY=${REZ_TINYXML_ROOT}/lib/libtinyxml.a

echo -e "\n"
echo -e "[CONFIGURE] Finished configuring OCIO-${OCIO_VERSION}!"
echo -e "\n"
