#!/usr/bin/bash

# Will exit the Bash script the moment any command will itself exit with a non-zero status, thus an error.
set -e

NUMPY_VERSION=$1
PYTHON_VERSION=${REZ_PYTHON_VERSION}
INSTALL_PATH=${REZ_BUILD_INSTALL_PATH}
TMP_DIR=${REZ_TMP_PATH}

# We print the arguments passed to the Bash script.
echo -e "\n"
echo -e "==============="
echo -e "=== INSTALL ==="
echo -e "==============="
echo -e "\n"

echo -e "[INSTALL][ARGS] NUMPY VERSION: ${NUMPY_VERSION}"
echo -e "[INSTALL][ARGS] PYTHON VERSION: ${PYTHON_VERSION}"
echo -e "[INSTALL][ARGS] INSTALL PATH: ${INSTALL_PATH}"
echo -e "[INSTALL][ARGS] TEMP DIR: ${TMP_DIR}"

# We check if the arguments variables we need are correctly set.
# If not, we abort the process.
if [[ -z ${NUMPY_VERSION} || -z ${INSTALL_PATH} || -z ${PYTHON_VERSION} || -z ${TMP_DIR} ]]; then
    echo -e "\n"
    echo -e "[INSTALL][ARGS] One or more of the argument variables are empty. Aborting..."
    echo -e "\n"

    exit 1
fi

# We install Python.
echo -e "\n"
echo -e "[INSTALL] Installing numpy-${NUMPY_VERSION}..."
echo -e "\n"

rez-pip --python-version ${PYTHON_VERSION} -i -p ${TMP_DIR} numpy==${NUMPY_VERSION}

cd ${TMP_DIR}/numpy/${NUMPY_VERSION}
cd $(ls -d */|head -n 1)
cp -r ./bin ${INSTALL_PATH}
cp -r ./python/* ${INSTALL_PATH}

echo -e "\n"
echo -e "[INSTALL] Finished installing numpy-${NUMPY_VERSION}!"
echo -e "\n"
