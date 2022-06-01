# Based and improved from https://github.com/piratecrew/rez-python
# Then taken from OSS-Pipeline from https://github.com/OSS-Pipeline/rez-python

name = "python"

version = "3.6.4"

authors = [
    "Guido van Rossum"
]

description = \
    """
    The Python programming language.
    """

requires = [
    "cmake-3+",
    "gcc-6+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "2to3",
    "idle",
    "pip",
    "pip3.7",
    "pip3",
    "pydoc",
    "python-config",
    "python",
    "python3-config",
    "python3.7-config",
    "python3.7",
    "python3",
    "smtpd.py"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "python-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")

    # Helper environment variables.
    env.PYTHON_BINARY_PATH.set("{root}/bin")
    env.PYTHON_INCLUDE_PATH.set("{root}/include")
    env.PYTHON_LIBRARY_PATH.set("{root}/lib")
