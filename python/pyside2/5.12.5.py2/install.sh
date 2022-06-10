#!/usr/bin/bash

# Will exit the Bash script the moment any command will itself exit with a non-zero status, thus an error.
set -e

INSTALL_PATH=${REZ_BUILD_INSTALL_PATH}
PYSIDE_URL=$1
PYSIDE_VERSION=${REZ_BUILD_PROJECT_VERSION}

# We print the arguments passed to the Bash script.
echo -e "\n"
echo -e "==============="
echo -e "=== INSTALL ==="
echo -e "==============="
echo -e "\n"

echo -e "[INSTALL][ARGS] INSTALL PATH: ${INSTALL_PATH}"
echo -e "[INSTALL][ARGS] PYSIDE2 URL: ${PYSIDE_URL}"
echo -e "[INSTALL][ARGS] PYSIDE2 VERSION: ${PYSIDE_VERSION}"

# We check if the arguments variables we need are correctly set.
# If not, we abort the process.
if [[ -z ${INSTALL_PATH} || -z ${PYSIDE_URL} || -z ${PYSIDE_VERSION} ]]; then
    echo -e "\n"
    echo -e "[INSTALL][ARGS] One or more of the argument variables are empty. Aborting..."
    echo -e "\n"

    exit 1
fi

# We install PySide2.
echo -e "\n"
echo -e "[INSTALL] Installing PySide2-${PYSIDE_VERSION}..."
echo -e "\n"

# We copy the necessary files to the install directory.
pip2 \
    install ${PYSIDE_URL} \
    --target ${INSTALL_PATH} \
    --upgrade \
    --no-dependencies

echo -e "\n"
echo -e "[INSTALL] Finished installing PySide2-${PYSIDE_VERSION}!"
echo -e "\n"
