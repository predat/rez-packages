#!/bin/bash

v=(${REZ_BUILD_PROJECT_VERSION//./ })
# because bash3 on macOS
n=$(tr '[:lower:]' '[:upper:]' <<< ${REZ_BUILD_PROJECT_NAME:0:1})${REZ_BUILD_PROJECT_NAME:1}
ARCHIVE="${REZ_BUILD_PROJECT_NAME}-${REZ_BUILD_PROJECT_VERSION}"

if [ "$REZ_PLATFORM_VERSION" == 'linux' ]; then
    ARCHIVE="${ARCHIVE}-linux-x64"
    EXTENSION="tar.xz"
    DOWNLOAD_URL="https://ftp.halifax.rwth-aachen.de/blender/release/Blender${v[0]}.${v[1]}/${ARCHIVE}.${EXTENSION}"
    if [[ ! -f ${ARCHIVE}.${EXTENSION} ]]; then
        echo "- Download $DOWNLOAD_URL"
        curl -O ${DOWNLOAD_URL}
    fi
    mkdir -p $REZ_BUILD_INSTALL_PATH
    tar -xf "${ARCHIVE}.${EXTENSION}" -C "${REZ_BUILD_INSTALL_PATH}" --strip-components=1
else
    ARCHIVE="${ARCHIVE}-windows-x64"
    EXTENSION="zip"
    DOWNLOAD_URL="https://ftp.nluug.nl/pub/graphics/blender/release/${n}${v[0]}.${v[1]}/${ARCHIVE}.${EXTENSION}"
    if [[ ! -f ${ARCHIVE}.${EXTENSION} ]]; then
        echo "- Download $DOWNLOAD_URL"
        curl --insecure -O ${DOWNLOAD_URL}
    fi
    unzip ${ARCHIVE}.${EXTENSION}
    cp -ar blender-${v[0]}.${v[1]}.${v[2]}-windows-x64/* ${REZ_BUILD_INSTALL_PATH}
fi
