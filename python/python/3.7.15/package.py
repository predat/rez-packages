# -*- coding: utf-8 -*-


name = "pythonStandalone"

def _version():
    import os
    return os.path.basename(os.getcwd())

version = _version()

authors = ["Guido van Rossum"]

description = """The Python programming language."""

# requires = [
# ]

private_build_requires = [
    "gcc-12",
    "cmake-3",
    #"zlib-1.2",
    #"xz-5.2",
    #"libffi-3.4",
    #"expat-2.5",
    #"mpdecimal-2.5",
    "openssl-3.0"]  # rpath is set to REZ_OPENSSL_ROOT

variants = [
    ["platform-linux", "build-release"],
    ["platform-linux", "build-debug"]
]

tools = [
    "2to3",
    "idle",
    "pydoc",
    "python3",
    "python3.11",
    "python3.11-config",
    "python3-config",
    "python-config",
    "smtpd.py"
]

uuid = "repository.{}".format(name)


with scope("config") as config:
    config.release_packages_path = "/s/apps/packages/dev"


def commands():
    import os.path

    env.PATH.prepend(os.path.join("{root}", "bin"))
    env.LD_LIBRARY_PATH.append(os.path.join("{root}", "lib"))

    alias('python', os.path.join("{root}", "bin", "python3"))

    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")
        env.PKG_CONFIG_PATH.prepend(os.path.join("{root}", "lib", "pkgconfig"))

