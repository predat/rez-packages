#!/bin/bash


# Need by qt5
source /opt/rh/devtoolset-7/enable


cd "${REZ_BUILD_PATH}"
git clone --recursive https://code.qt.io/pyside/pyside-setup
cd pyside-setup
git checkout v"${REZ_BUILD_PROJECT_VERSION}"



#
# shiboken2
echo "--- Building shiboken2"
cd sources/shiboken2
mkdir build
cd build

cmake .. -DCMAKE_INSTALL_PREFIX="${REZ_BUILD_INSTALL_PATH}"
make -j12 install
cd ../..



#
# PySide2
echo "--- Building PySide2"
cd pyside2
mkdir build
cd build

cmake .. -DCMAKE_INSTALL_PREFIX="${REZ_BUILD_INSTALL_PATH}" -DShiboken2_DIR="${REZ_BUILD_INSTALL_PATH}/lib/cmake"
make -j12 install
cd ../..



#
# Pyside2-tools
echo "Building PySide-tools"
cd pyside2-tools
mkdir build
cd build

cmake .. -DCMAKE_INSTALL_PREFIX="${REZ_BUILD_INSTALL_PATH}"
make -j12 install
cd ../..
