#!/usr/bin/bash

# Will exit the Bash script the moment any command will itself exit with a non-zero status, thus an error.
set -e

EXTRACT_PATH=$1
BUILD_PATH=$2
INSTALL_PATH=${REZ_BUILD_INSTALL_PATH}
PYILMBASE_VERSION=${REZ_BUILD_PROJECT_VERSION}

# We print the arguments passed to the Bash script.
echo -e "\n"
echo -e "================="
echo -e "=== CONFIGURE ==="
echo -e "================="
echo -e "\n"

echo -e "[CONFIGURE][ARGS] EXTRACT PATH: ${EXTRACT_PATH}"
echo -e "[CONFIGURE][ARGS] BUILD PATH: ${BUILD_PATH}"
echo -e "[CONFIGURE][ARGS] INSTALL PATH: ${INSTALL_PATH}"
echo -e "[CONFIGURE][ARGS] PYILMBASE VERSION: ${PYILMBASE_VERSION}"

# We check if the arguments variables we need are correctly set.
# If not, we abort the process.
if [[ -z ${EXTRACT_PATH} || -z ${BUILD_PATH} || -z ${INSTALL_PATH} || -z ${PYILMBASE_VERSION} ]]; then
    echo -e "\n"
    echo -e "[CONFIGURE][ARGS] One or more of the argument variables are empty. Aborting..."
    echo -e "\n"

    exit 1
fi

# We run the configuration script of PyIlmBase.
echo -e "\n"
echo -e "[CONFIGURE] Running the configuration script from PyIlmBase-${PYILMBASE_VERSION}..."
echo -e "\n"

mkdir -p ${BUILD_PATH}
cd ${BUILD_PATH}

# We detect Python and its components in a more modern fashion.
sed "s|FIND_PACKAGE ( PythonLibs REQUIRED )||1" --in-place ${BUILD_PATH}/../CMakeLists.txt
sed "s|FIND_PACKAGE ( PythonInterp REQUIRED )|find_package (Python REQUIRED \${PYTHON_VERSION} COMPONENTS Interpreter Development NumPy)|1" --in-place ${BUILD_PATH}/../CMakeLists.txt
sed "s|COMPONENTS Python|OPTIONAL_COMPONENTS python python\${REZ_PYTHON_MAJOR_VERSION} python\${REZ_PYTHON_MAJOR_VERSION}.\${REZ_PYTHON_MINOR_VERSION}|1" --in-place ${BUILD_PATH}/../CMakeLists.txt
sed "s|FIND_PACKAGE ( NumPy )||1" --in-place ${BUILD_PATH}/../CMakeLists.txt
sed "s|IF (NUMPY_FOUND)|IF (Python_NumPy_FOUND)|1" --in-place ${BUILD_PATH}/../CMakeLists.txt

# The name of some variables generated changed when using the more modern Python detection, so we have to update some scripts to reflect that.
sed "s|python\${PYTHON_VERSION_MAJOR}.\${PYTHON_VERSION_MINOR}|python\${Python_VERSION_MAJOR}.\${Python_VERSION_MINOR}|1" --in-place ${BUILD_PATH}/../PyIex/CMakeLists.txt ${BUILD_PATH}/../PyImath/CMakeLists.txt ${BUILD_PATH}/../PyImathNumpy/CMakeLists.txt

# PyIlmBase < 2.4.x is not installing the headers alongside the libraries, so we are going to do that ourselves.
mkdir -p ${INSTALL_PATH}/include/OpenEXR
cp "${BUILD_PATH}/../PyIex"/*.h ${INSTALL_PATH}/include/OpenEXR
cp "${BUILD_PATH}/../PyImath"/*.h ${INSTALL_PATH}/include/OpenEXR

# We make sure CMake is going to find some headers by adding them into CXX_FLAGS.
# We are not using version for finding the IlmBase libraries as it tends to very easily break.
cmake \
    ${BUILD_PATH}/.. \
    -DCMAKE_INSTALL_PREFIX=${INSTALL_PATH} \
    -DCMAKE_C_FLAGS="-fPIC" \
    -DCMAKE_CXX_FLAGS="-fPIC -I${REZ_PYTHON_ROOT}/include/python${REZ_PYTHON_MAJOR_VERSION}.${REZ_PYTHON_MINOR_VERSION} -I${REZ_BOOST_ROOT}/include -I${REZ_NUMPY_ROOT}/numpy/core/include" \
    -DNAMESPACE_VERSIONING=OFF \
    -DBOOST_ROOT=${REZ_BOOST_ROOT} \
    -DILMBASE_PACKAGE_PREFIX=${REZ_ILMBASE_ROOT}

echo -e "\n"
echo -e "[CONFIGURE] Finished configuring PyIlmBase-${PYILMBASE_VERSION}!"
echo -e "\n"
