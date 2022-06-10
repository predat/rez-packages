#!/usr/bin/bash

# Will exit the Bash script the moment any command will itself exit with a non-zero status, thus an error.
set -e

EXTRACT_PATH=$1
BUILD_PATH=$2
INSTALL_PATH=${REZ_BUILD_INSTALL_PATH}
USD_VERSION=${REZ_BUILD_PROJECT_VERSION}

# We print the arguments passed to the Bash script.
echo -e "\n"
echo -e "================="
echo -e "=== CONFIGURE ==="
echo -e "================="
echo -e "\n"

echo -e "[CONFIGURE][ARGS] EXTRACT PATH: ${EXTRACT_PATH}"
echo -e "[CONFIGURE][ARGS] BUILD PATH: ${BUILD_PATH}"
echo -e "[CONFIGURE][ARGS] INSTALL PATH: ${INSTALL_PATH}"
echo -e "[CONFIGURE][ARGS] USD VERSION: ${USD_VERSION}"

# We check if the arguments variables we need are correctly set.
# If not, we abort the process.
if [[ -z ${EXTRACT_PATH} || -z ${BUILD_PATH} || -z ${INSTALL_PATH} || -z ${USD_VERSION} ]]; then
    echo -e "\n"
    echo -e "[CONFIGURE][ARGS] One or more of the argument variables are empty. Aborting..."
    echo -e "\n"

    exit 1
fi

# We run the configuration script of USD.
echo -e "\n"
echo -e "[CONFIGURE] Running the configuration script from USD-${USD_VERSION}..."
echo -e "\n"

mkdir -p ${BUILD_PATH}
cd ${BUILD_PATH}

# The OCIO CMake script is only looking at "/lib", leaving out "/lib64" in the process.
sed "s| lib/| lib/ /lib64|1" --in-place ${EXTRACT_PATH}/cmake/modules/FindOpenImageIO.cmake

# The OpenEXR CMake script is assuming that OpenEXR and IlmBase includes and libraries are found in the same location,
# which is not necessarily the case. So we add an additional "ILMBASE_LOCATION" variable to use if that's the case.
sed "s|\"\${OPENEXR_LOCATION}\"|\"\${OPENEXR_LOCATION}\" \"\${ILMBASE_LOCATION}\"|1" --in-place ${EXTRACT_PATH}/cmake/modules/FindOpenEXR.cmake

# We manually had the compilers flags for OpenGL related libraries as it can happen that on too fresh CentOS images,
# the LD_LIBRARY_PATH environment variable is not even setup properly with the bare minimum paths.
cmake \
    ${BUILD_PATH}/.. \
    -DCMAKE_INSTALL_PREFIX=${INSTALL_PATH} \
    -DCMAKE_C_FLAGS="-fPIC" \
    -DCMAKE_CXX_FLAGS="-fPIC -I/usr/lib64 -I/usr/lib -lGLU -lglut -lGL -lutil -openmp -fopenmp" \
    -DCMAKE_POLICY_DEFAULT_CMP0072=NEW \
    -DCMAKE_POLICY_DEFAULT_CMP0074=NEW \
    -DPXR_BUILD_DOCUMENTATION=OFF \
    -DPXR_BUILD_EMBREE_PLUGIN=OFF \
    -DPXR_BUILD_IMAGING=ON \
    -DPXR_BUILD_MATERIALX_PLUGIN=OFF \
    -DPXR_BUILD_OPENCOLORIO_PLUGIN=ON \
    -DPXR_BUILD_OPENIMAGEIO_PLUGIN=ON \
    -DPXR_BUILD_PRMAN_PLUGIN=OFF \
    -DPXR_BUILD_TESTS=ON \
    -DPXR_BUILD_USDVIEW=ON \
    -DPXR_BUILD_USD_IMAGING=ON \
    -DPXR_ENABLE_GL_SUPPORT=ON \
    -DPXR_ENABLE_HDF5_SUPPORT=OFF \
    -DPXR_ENABLE_NAMESPACES=ON \
    -DPXR_ENABLE_OSL_SUPPORT=OFF \
    -DPXR_ENABLE_PTEX_SUPPORT=ON \
    -DPXR_ENABLE_PYTHON_SUPPORT=ON \
    -DPXR_HEADLESS_TEST_MODE=OFF \
    -DPXR_STRICT_BUILD_MODE=OFF \
    -DPXR_VALIDATE_GENERATED_CODE=OFF \
    -DBoost_NO_BOOST_CMAKE=ON \
    -DBoost_NO_SYSTEM_PATHS=ON \
    -DBOOST_ROOT=${REZ_BOOST_ROOT} \
    -DGLEW_LOCATION=${REZ_GLEW_ROOT} \
    -DILMBASE_LOCATION=${REZ_ILMBASE_ROOT} \
    -DOCIO_LOCATION=${REZ_OCIO_ROOT} \
    -DOIIO_LOCATION=${REZ_OIIO_ROOT} \
    -DOPENEXR_LOCATION=${REZ_OPENEXR_ROOT} \
    -DOPENSUBDIV_ROOT_DIR=${REZ_OPENSUBDIV_ROOT} \
    -DPTEX_LOCATION=${REZ_PTEX_ROOT} \
    -DTBB_ROOT_DIR=${REZ_TBB_ROOT}

echo -e "\n"
echo -e "[CONFIGURE] Finished configuring USD-${USD_VERSION}!"
echo -e "\n"
