name = "python"

version = "2.7.12"

authors = [
    "Guido van Rossum"
]

description = \
    """
    The Python programming language.
    """

build_requires = [
    #"gcc-4.8.2"
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

tools = [
    "2to3",
    "idle",
    "pydoc",
    "python",
    "python2",
    "python2.7",
    "python2.7-config",
    "python2-config",
    "python-config",
    "smtpd.py"
]

uuid = "repository.python"


def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.PYTHON_INCLUDE_DIR = "{root}/include/python2.7"
        env.PYTHON_LIBRARIES = "{root}/lib/python2.7/config/libpython2.7.a"
