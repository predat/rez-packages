#!/bin/bash

srcpath=$1
destpath=$2

pyver="${REZ_PYTHON_MAJOR_VERSION}.${REZ_PYTHON_MINOR_VERSION}"
pypath=${destpath}/lib/python${pyver}/site-packages
mkdir -p ${pypath} &> /dev/null

cd ${srcpath}
#PYTHONPATH=$PYTHONPATH:${pypath} python setup.py --with-libyaml install --prefix=${destpath}
#export CPPFLAGS=-I$REZ_LIBYAML_ROOT/include
export LDFLAGS=-L${REZ_LIBYAML_ROOT}/lib
export CFLAGS=-I${REZ_LIBYAML_ROOT}/include

echo "---------------------- $LDFLAGS"
echo "---------------------- $CFLAGS"

PYTHONPATH=$PYTHONPATH:${pypath} python setup.py build_ext -I "${REZ_LIBYAML_ROOT}/include" -L "${REZ_LIBYAML_ROOT}/lib" install --prefix=${destpath}

mkdir -p ${destpath}/python &> /dev/null
cp -rf ${pypath}/* ${destpath}/python/
rm -rf ${destpath}/lib
