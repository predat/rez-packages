#!/bin/bash


if [[ $MAYA_VERSION == "2016" ]]; then

    INSTALL_PACKAGE="mentalray_Plugin_for_Maya_2016_SP6_EN_Linux_64bit.tgz"

else

    INSTALL_PACKAGE="mentalray_Plugin_for_Maya_2016_EXT2_SP2_EN_Linux_64bit.tgz"

fi

#
echo "Extract archive"

tar -xf "${REZ_BUILD_SOURCE_PATH}/archives/${INSTALL_PACKAGE}" -C "${REZ_BUILD_PATH}"


echo "Extract rpm"

cd "${REZ_BUILD_PATH}"

for rpm_file in mentalray*.rpm;
do
    rpm2cpio "${rpm_file}" | cpio -idm -W none;
done


#
echo "Copying files"

cd "${REZ_BUILD_PATH}/usr/autodesk/mentalrayForMaya${MAYA_VERSION}"

for file in *
do
    echo "Installing: ${file}"
    cp -rf "${file}" "${REZ_BUILD_INSTALL_PATH}"
done

cd "${REZ_BUILD_PATH}/usr/autodesk/modules/maya/${MAYA_VERSION}"
echo "Installing: module"
sed -i "s/<MENTALRAY_DIR>/./g" mentalray.mod
cp -rf mentalray.mod "${REZ_BUILD_INSTALL_PATH}"



