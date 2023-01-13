#!/bin/bash

ARCHIVE="google-chrome-stable-${REZ_BUILD_PROJECT_VERSION}-1.x86_64.rpm"
URL="https://dl.google.com/linux/chrome/rpm/stable/x86_64/${ARCHIVE}"


if [[ ! -f $REZ_BUILD_SOURCE_PATH/$ARCHIVE ]]; then
    wget -P $REZ_BUILD_SOURCE_PATH $URL
fi


if [[ $1 == "install" ]]; then

    rpm2cpio ${REZ_BUILD_SOURCE_PATH}/$ARCHIVE | cpio -idvm

    cp -ar opt/google/chrome/* "$REZ_BUILD_INSTALL_PATH"
    sudo -- sh -c "chown root: "$REZ_BUILD_INSTALL_PATH"/chrome-sandbox && chmod 4755 "$REZ_BUILD_INSTALL_PATH"/chrome-sandbox"
fi
