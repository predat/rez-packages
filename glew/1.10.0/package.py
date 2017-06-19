name = "glew"

version = "1.10.0"

authors = [
    "Nigel Stewart"
]

description = \
    """
    OpenGL Extension Wrangler
    """

build_requires = ["gcc-4.8.3"]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-6.8"]
]

uuid = "repository.glew"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.GLEW_INCLUDE_DIR = "{root}/include"
    env.PKG_CONFIG_PATH.append("{root}/lib64/pkgconfig")
