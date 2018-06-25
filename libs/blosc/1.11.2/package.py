name = "blosc"

version = "1.11.2"

authors = [
    "blosc"
]

description = \
    """
    A blocking, shuffling and loss-less compression library
    that can be faster than `memcpy()`.
    """

requires = [
]

build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64"],
]

uuid = "repository.blosc"

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")

