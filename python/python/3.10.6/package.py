# Based and improved from https://github.com/piratecrew/rez-python
# Then taken from OSS-Pipeline from https://github.com/OSS-Pipeline/rez-python

name = "python"

version = "3.10.6"

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
    "pip3.6",
    "pip3",
    "pydoc",
    "python-config",
    "python",
    "python3-config",
    "python3.6-config",
    "python3.6",
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
    env.PYTHON_INCLUDE_PATH.set("{root}/include/python3.10m")
    env.PYTHON_LIBRARY_PATH.set("{root}/lib")

    env.PYTHON_INCLUDE_DIR = "{root}/include/python3.10m"

    env.PYTHONPATH.prepend("{root}")

    # these are the builtin modules for this python executable. If we don't
    # include these, some python behavior can be incorrect.
    #  import os
    #  import os.path
    #
    #  path = os.path.join(this.root, "python")  # noqa
    #  for dirname in os.listdir(path):
        #  path_ = os.path.join(path, dirname)
        #  env.PYTHONPATH.append(path_)
