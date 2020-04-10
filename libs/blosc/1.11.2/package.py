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

private_build_requires = ['gcc-6.3.1']

variants = [["platform-linux"]]

uuid = "repository.blosc"

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")

