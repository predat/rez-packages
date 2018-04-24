#!/usr/bin/env bash
BINARY_DIR=$1
SOURCE_DIR=$2

echo "BINARY:  " + $BINARY_DIR # /prod/apps/rez/repository/maxwell/4.1.2/plugin/build/maya-2017
echo "SOURCE:  " + $SOURCE_DIR # /prod/apps/rez/repository/maxwell/4.1.2/plugin

echo "Extracting Maxwell plugin for Maya ${MAYA_VERSION}."
MAYA_VERSION_SHORT=$(echo ${MAYA_VERSION} | ( IFS=".$IFS" ; read a b && echo $a ))
cd $BINARY_DIR/maxwell/src/maxwell
tar -zxvf maxwell-maya${MAYA_VERSION_SHORT}_${REZ_BUILD_PROJECT_VERSION}.tar.gz
