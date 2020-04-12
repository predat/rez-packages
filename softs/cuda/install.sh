#!/bin/bash

wget https://developer.nvidia.com/compute/cuda/9.2/Prod2/local_installers/cuda_9.2.148_396.37_linux
chmod 744 cuda_9.2.148_396.37_linux
./cuda_9.2.148_396.37_linux --silent \
    --toolkit \
    --toolkitpath=${REZ_BUILD_INSTALL_PATH} \
    --no-opengl-libs \
    --no-drm \
    --verbose

# wget https://developer.nvidia.com/compute/cuda/9.2/Prod2/patches/1/cuda_9.2.148.1_linux
# chmod 755 cuda_9.2.148.1_linux
# ./cuda_9.2.148.1_linux --silent \
#     --toolkit \
#     --toolkitpath=${REZ_BUILD_INSTALL_PATH} \
#     --no-opengl-libs \
#     --no-drm \
#     --verbose

