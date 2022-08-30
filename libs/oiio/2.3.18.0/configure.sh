#!/usr/bin/bash

# Will exit the Bash script the moment any command will itself exit with a non-zero status, thus an error.
set -e

EXTRACT_PATH=$1
BUILD_PATH=$2
INSTALL_PATH=${REZ_BUILD_INSTALL_PATH}
OIIO_VERSION=${REZ_BUILD_PROJECT_VERSION}

# We print the arguments passed to the Bash script.
echo -e "\n"
echo -e "================="
echo -e "=== CONFIGURE ==="
echo -e "================="
echo -e "\n"

echo -e "[CONFIGURE][ARGS] EXTRACT PATH: ${EXTRACT_PATH}"
echo -e "[CONFIGURE][ARGS] BUILD PATH: ${BUILD_PATH}"
echo -e "[CONFIGURE][ARGS] INSTALL PATH: ${INSTALL_PATH}"
echo -e "[CONFIGURE][ARGS] OIIO VERSION: ${OIIO_VERSION}"

# We check if the arguments variables we need are correctly set.
# If not, we abort the process.
if [[ -z ${EXTRACT_PATH} || -z ${BUILD_PATH} || -z ${INSTALL_PATH} || -z ${OIIO_VERSION} ]]; then
    echo -e "\n"
    echo -e "[CONFIGURE][ARGS] One or more of the argument variables are empty. Aborting..."
    echo -e "\n"

    exit 1
fi

# We run the configuration script of OIIO.
echo -e "\n"
echo -e "[CONFIGURE] Running the configuration script from OIIO-${OIIO_VERSION}..."
echo -e "\n"

mkdir -p ${BUILD_PATH}
cd ${BUILD_PATH}

# sed "s|find_package (PythonLibs \${PYTHON_VERSION} REQUIRED)|find_package (Python \${PYTHON_VERSION} REQUIRED COMPONENTS Interpreter Development NumPy)|1" --in-place ${EXTRACT_PATH}/src/python/CMakeLists.txt

# We disable the support for PNG for now, as it seems to cause issues for building OSL, which ends up trying to link
# our own version of libpng against the system version of libz, which can be too old and create undefined reference
# for "oslc", but strangely not for "testshade_dso".
cmake \
    ${BUILD_PATH}/.. \
    -DCMAKE_INSTALL_PREFIX=${INSTALL_PATH} \
    -DCMAKE_C_FLAGS="-fPIC" \
    -DCMAKE_CXX_FLAGS="-fPIC" \
    -DCMAKE_POLICY_DEFAULT_CMP0072=NEW \
    -DCMAKE_POLICY_DEFAULT_CMP0074=NEW \
    -DOIIO_BUILD_TESTS=OFF \
    -DOIIO_BUILD_TOOLS=ON \
    -DUSE_EXTERNAL_PUGIXML=ON \
    -DUSE_FFMPEG=OFF \
    -DUSE_FIELD3D=OFF \
    -DUSE_FREETYPE=OFF \
    -DUSE_GIF=OFF \
    -DUSE_JPEGTURBO=ON \
    -DUSE_LIBCPLUSPLUS=OFF \
    -DUSE_LIBRAW=OFF \
    -DUSE_NUKE=OFF \
    -DUSE_OCIO=ON \
    -DUSE_OPENCV=OFF \
    -DUSE_OPENGL=OFF \
    -DUSE_OPENJPEG=ON \
    -DUSE_OPENSSL=OFF \
    -DUSE_PTEX=ON \
    -DUSE_PYTHON=OFF \
    -DUSE_QT=OFF \
    -DVERBOSE=ON \
    -DBoost_NO_BOOST_CMAKE=ON \
    -DBoost_NO_SYSTEM_PATHS=ON \
    -DBOOST_ROOT=${REZ_BOOST_ROOT} \
    -DIMATH_INCLUDE_PATH=${REZ_IMATH_ROOT}/include \
    -DJPEG_INCLUDE_DIR=${REZ_JPEG_TURBO_ROOT}/include \
    -DOpenColorIO_ROOT=${REZ_OCIO_ROOT} \
    -DOPENEXR_INCLUDE_PATH=${REZ_OPENEXR_ROOT}/include \
    -DOpenJPEG_ROOT=${REZ_OPENJPEG_ROOT} \
    -DPNG_ROOT=${REZ_PNG_ROOT} \
    -DPUGIXML_INCLUDE_DIR=${REZ_PUGIXML_ROOT}/include \
    -DPUGIXML_LIBRARY=${REZ_PUGIXML_ROOT}/lib/libpugixml.so \
    -DTBB_ROOT=${REZ_TBB_ROOT} \
    -DTIFF_ROOT=${REZ_TIFF_ROOT} \
    -DZLIB_ROOT=${REZ_ZLIB_ROOT}

echo -e "\n"
echo -e "[CONFIGURE] Finished configuring OIIO-${OIIO_VERSION}!"
echo -e "\n"
