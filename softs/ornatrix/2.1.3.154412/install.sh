#!/bin/bash


# export

#  REZ_BUILD_INSTALL_PATH
#  REZ_BUILD_PATH

sh /prod/prod2/Projets/RESSOURCES/_LIB/INSTALLS/clean/ornatrix/2.1.3.15412/Ornatrix-Maya-2-1-3-15412-linux_343420342036373336.run --target "${REZ_BUILD_PATH}" --noexec

cp -r "${REZ_BUILD_PATH}/Ephere" "${REZ_BUILD_INSTALL_PATH}"
cp -r "${REZ_BUILD_PATH}/Ornatrix.mod" "${REZ_BUILD_INSTALL_PATH}"

sed -i 's/\/opt/./g' "${REZ_BUILD_INSTALL_PATH}/Ornatrix.mod"

# Remove unused files
rm "${REZ_BUILD_INSTALL_PATH}/Ephere/LicenseManager.sh"
rm "${REZ_BUILD_INSTALL_PATH}/Ephere/LicenseServer.sh"
rm "${REZ_BUILD_INSTALL_PATH}/Ephere/Ephere.Licensing.LicenseServer.Manager.exe"

# copy License file
cp "${REZ_BUILD_SOURCE_PATH}/config/OrnatrixMayaLicenseServerIP.txt" "${REZ_BUILD_INSTALL_PATH}"
