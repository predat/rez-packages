#!/usr/bin/bash

# Will exit the Bash script the moment any command will itself exit with a non-zero status, thus an error.
set -e

EXTRACT_PATH=$1
INSTALL_PATH=${REZ_BUILD_INSTALL_PATH}
BOOST_VERSION=${REZ_BUILD_PROJECT_VERSION}

# We print the arguments passed to the Bash script.
echo -e "\n"
echo -e "================="
echo -e "=== CONFIGURE ==="
echo -e "================="
echo -e "\n"

echo -e "[CONFIGURE][ARGS] EXTRACT PATH: ${EXTRACT_PATH}"
echo -e "[CONFIGURE][ARGS] INSTALL PATH: ${INSTALL_PATH}"
echo -e "[CONFIGURE][ARGS] BOOST VERSION: ${BOOST_VERSION}"

# We check if the arguments variables we need are correctly set.
# If not, we abort the process.
if [[ -z ${EXTRACT_PATH} || -z ${INSTALL_PATH} || -z ${BOOST_VERSION} ]]; then
    echo -e "\n"
    echo -e "[CONFIGURE][ARGS] One or more of the argument variables are empty. Aborting..."
    echo -e "\n"

    exit 1
fi

# We run the configuration script of Boost.
echo -e "\n"
echo -e "[CONFIGURE] Running the configuration script from Boost-${BOOST_VERSION}..."
echo -e "\n"

cd ${EXTRACT_PATH}

${EXTRACT_PATH}/bootstrap.sh \
    --prefix=${INSTALL_PATH} \
    --with-python=${REZ_PYTHON_ROOT}/bin/python \
    --with-python-root=${REZ_PYTHON_ROOT}

# Configure user-config.jam for the write python folder
touch ${HOME}/user-config.jam
echo -n "echo using python : ${REZ_PYTHON_VERSION} : ${PYTHON_BINARY_PATH} : ${PYTHON_INCLUDE_PATH} : ${PYTHON_LIBRARY_PATH} ; > ${HOME}/user-config.jam"
echo "using python : ${REZ_PYTHON_VERSION} : ${PYTHON_BINARY_PATH} : ${PYTHON_INCLUDE_PATH} : ${PYTHON_LIBRARY_PATH} ;" >> ${HOME}/user-config.jam

echo -e "\n"
echo -e "[CONFIGURE] Finished configuring Boost-${BOOST_VERSION}!"
echo -e "\n"
