# -*- coding: utf-8 -*-


name = 'openssl'

def _version():
    import os
    return os.path.basename(os.getcwd())

version = _version()

description = """
The Open Source toolkit for Secure Sockets Layer and Transport Layer Security
"""

private_build_requires = [
    'gcc-9+',
    'cmake-3',
    'zlib-1.2'
]

variants = [["platform-linux"]]

tools = [
    'openssl',
    'c_rehash'
]

# with scope("config") as config:
#     config.release_packages_path = "/s/apps/packages/dev"


def commands():
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')

    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
