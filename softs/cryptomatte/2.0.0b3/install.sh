#!/bin/bash

BINARY_DIR=$1
PREFIX_DIR=$2
# MAJOR_VERSION=$3


echo "--- bin   : $BINARY_DIR"
echo "--- prefix: $PREFIX_DIR"

# cryptomatte_arnold/src/cryptomatte_arnold

cp -ra "$BINARY_DIR/cryptomatte_arnold/src/cryptomatte_arnold/ae" "$PREFIX_DIR"
cp -ra "$BINARY_DIR/cryptomatte_arnold/src/cryptomatte_arnold/bin" "$PREFIX_DIR"
cp -ra "$BINARY_DIR/cryptomatte_arnold/src/cryptomatte_arnold/aexml" "$PREFIX_DIR"

