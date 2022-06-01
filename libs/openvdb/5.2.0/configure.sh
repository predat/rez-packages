#!/usr/bin/bash

# Will exit the Bash script the moment any command will itself exit with a non-zero status, thus an error.
set -e

EXTRACT_PATH=$1
BUILD_PATH=$2
INSTALL_PATH=${REZ_BUILD_INSTALL_PATH}
OPENVDB_VERSION=${REZ_BUILD_PROJECT_VERSION}

# We print the arguments passed to the Bash script.
echo -e "\n"
echo -e "================="
echo -e "=== CONFIGURE ==="
echo -e "================="
echo -e "\n"

echo -e "[CONFIGURE][ARGS] EXTRACT PATH: ${EXTRACT_PATH}"
echo -e "[CONFIGURE][ARGS] BUILD PATH: ${BUILD_PATH}"
echo -e "[CONFIGURE][ARGS] INSTALL PATH: ${INSTALL_PATH}"
echo -e "[CONFIGURE][ARGS] OPENVDB VERSION: ${OPENVDB_VERSION}"

# We check if the arguments variables we need are correctly set.
# If not, we abort the process.
if [[ -z ${EXTRACT_PATH} || -z ${BUILD_PATH} || -z ${INSTALL_PATH} || -z ${OPENVDB_VERSION} ]]; then
    echo -e "\n"
    echo -e "[CONFIGURE][ARGS] One or more of the argument variables are empty. Aborting..."
    echo -e "\n"

    exit 1
fi

# We run the configuration script of OpenVDB.
echo -e "\n"
echo -e "[CONFIGURE] Running the configuration script from OpenVDB-${OPENVDB_VERSION}..."
echo -e "\n"

mkdir -p ${BUILD_PATH}
cd ${BUILD_PATH}

# We modify this CMakeLists file so that we can find boost::python in case we don't have the Python version embedded in the built library as a build ID for example.
sed "s|REQUIRED COMPONENTS python\${PYTHON_VERSION_MAJOR}.\${PYTHON_VERSION_MINOR}|OPTIONAL_COMPONENTS python python\${PYTHON_VERSION_MAJOR} python\${PYTHON_VERSION_MAJOR}.\${PYTHON_VERSION_MINOR}|1" --in-place ${BUILD_PATH}/../openvdb/python/CMakeLists.txt

# We use the OpenVDB ABI 5, i.e. Houdini 17 and later. Maya should technically be compatible with any OpenVDB ABI.
cmake \
    ${BUILD_PATH}/.. \
    -DCMAKE_INSTALL_PREFIX=${INSTALL_PATH} \
    -DCMAKE_C_FLAGS="-fPIC" \
    -DCMAKE_CXX_FLAGS="-fPIC" \
    -DOPENVDB_ABI_VERSION_NUMBER="5" \
    -DOPENVDB_BUILD_BINARIES=ON \
    -DOPENVDB_BUILD_CORE=ON \
    -DOPENVDB_BUILD_DOCS=OFF \
    -DOPENVDB_BUILD_HOUDINI_PLUGIN=OFF \
    -DOPENVDB_BUILD_MAYA_PLUGIN=OFF \
    -DOPENVDB_BUILD_PYTHON_MODULE=ON \
    -DOPENVDB_BUILD_UNITTESTS=OFF \
    -DOPENVDB_BUILD_VDB_LOD=ON \
    -DOPENVDB_BUILD_VDB_PRINT=ON \
    -DOPENVDB_BUILD_VDB_RENDER=ON \
    -DOPENVDB_BUILD_VDB_VIEW=ON \
    -DUSE_GLFW3=ON \
    -DBLOSC_LOCATION=${REZ_BLOSC_ROOT} \
    -DBoost_NO_BOOST_CMAKE=ON \
    -DBoost_NO_SYSTEM_PATHS=ON \
    -DBOOST_ROOT=${REZ_BOOST_ROOT} \
    -DGLFW3_LOCATION=${REZ_GLFW_ROOT} \
    -DILMBASE_LOCATION=${REZ_ILMBASE_ROOT} \
    -DOPENEXR_LOCATION=${REZ_OPENEXR_ROOT} \
    -DTBB_LOCATION=${REZ_TBB_ROOT} \
    -DZLIB_ROOT=${REZ_ZLIB_ROOT}

echo -e "\n"
echo -e "[CONFIGURE] Finished configuring OpenVDB-${OPENVDB_VERSION}!"
echo -e "\n"
