#!/bin/bash

# export CXX=/opt/rh/devtoolset-7/root/usr/bin/g++
# export CC=/opt/rh/devtoolset-7/root/usr/bin/gcc
# export LDFLAGS="-static-libstdc++ -static-libgcc"

source /opt/rh/devtoolset-7/enable

eval "$*"
