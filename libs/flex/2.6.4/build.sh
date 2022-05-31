#!/usr/bin/bash

# Will exit the Bash script the moment any command will itself exit with a non-zero status, thus an error.
set -e

EXTRACT_PATH=$1
FLEX_VERSION=${REZ_BUILD_PROJECT_VERSION}

# We print the arguments passed to the Bash script.
echo -e "\n"
echo -e "============="
echo -e "=== BUILD ==="
echo -e "============="
echo -e "\n"

echo -e "[BUILD][ARGS] EXTRACT PATH: ${EXTRACT_PATH}"
echo -e "[BUILD][ARGS] FLEX VERSION: ${FLEX_VERSION}"

# We check if the arguments variables we need are correctly set.
# If not, we abort the process.
if [[ -z ${EXTRACT_PATH} || -z ${FLEX_VERSION} ]]; then
    echo -e "\n"
    echo -e "[BUILD][ARGS] One or more of the argument variables are empty. Aborting..."
    echo -e "\n"

    exit 1
fi

# We build flex.
echo -e "\n"
echo -e "[BUILD] Building flex-${FLEX_VERSION}..."
echo -e "\n"

cd ${EXTRACT_PATH}

make \
    -j${REZ_BUILD_THREAD_COUNT}

echo -e "\n"
echo -e "[BUILD] Finished building flex-${FLEX_VERSION}!"
echo -e "\n"
