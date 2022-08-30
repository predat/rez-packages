#!/usr/bin/bash

# Will exit the Bash script the moment any command will itself exit with a non-zero status, thus an error.
set -e

EXTRACT_PATH=$1
BUILD_PATH=$2
PYTHON_INCLUDE_PATH=${PYTHON_INCLUDE_PATH}
BOOST_VERSION=${REZ_BUILD_PROJECT_VERSION}

# We print the arguments passed to the Bash script.
echo -e "\n"
echo -e "==============="
echo -e "=== INSTALL ==="
echo -e "==============="
echo -e "\n"

echo -e "[INSTALL][ARGS] EXTRACT PATH: ${EXTRACT_PATH}"
echo -e "[INSTALL][ARGS] BUILD PATH: ${BUILD_PATH}"
echo -e "[INSTALL][ARGS] PYTHON INCLUDE PATH: ${PYTHON_INCLUDE_PATH}"
echo -e "[INSTALL][ARGS] BOOST VERSION: ${BOOST_VERSION}"

# We check if the arguments variables we need are correctly set.
# If not, we abort the process.
if [[ -z ${EXTRACT_PATH} || -z ${BUILD_PATH} || -z ${BOOST_VERSION} ]]; then
    echo -e "\n"
    echo -e "[CONFIGURE][ARGS] One or more of the argument variables are empty. Aborting..."
    echo -e "\n"

    exit 1
fi

# We install Boost.
echo -e "\n"
echo -e "[INSTALL] Installing Boost-${BOOST_VERSION}..."
echo -e "\n"

cd ${EXTRACT_PATH}

${EXTRACT_PATH}/b2 \
    -j${REZ_BUILD_THREAD_COUNT} \
    --build-dir=${BUILD_PATH} \
    cflags="-fPIC" \
    cxxflags="-fPIC" \
    link=shared link=static \
    -q \
    -s NO_BZIP2=1 \
    --toolset=gcc \
    threading=multi \
    release \
    install

echo -e "\n"
echo -e "[INSTALL] Finished installing Boost-${BOOST_VERSION}!"
echo -e "\n"
