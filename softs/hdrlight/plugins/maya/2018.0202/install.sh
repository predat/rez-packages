#!/bin/bash

echo "Extrat archive"
tar -xf "${REZ_BUILD_SOURCE_PATH}/archives/maya${MAYA_VERSION}_linux_${REZ_BUILD_PROJECT_VERSION}.tar.gz" -C "${REZ_BUILD_PATH}"


cd "${REZ_BUILD_PATH}/HDRLightStudioConnectionMaya/${MAYA_VERSION}"

sed -i "s/\~\/Lightmap\/HDRLightStudioConnectionMaya\/$MAYA_VERSION\//./g" HDRLightStudio.mod

for file in *
do
    echo "Copy $file into dest directory ${REZ_BUILD_INSTALL_PATH}"
    cp -ar "${file}" "${REZ_BUILD_INSTALL_PATH}"
done
