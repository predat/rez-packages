name = "shiboken2"

version = "5.12.5.py2"

authors = [
    "The Qt Company"
]

description = \
    """
    Shiboken is the Python binding generator that Qt for Python uses to create the PySide module, in other words,
    is the system we use to expose the Qt C++ API to Python.
    """

requires = [
    "cmake-3+",
    "python-2.7"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "shiboken2-{version}".format(version=str(version))

def commands():
    env.PYTHONPATH.prepend("{root}")

    # Helper environment variables.
    env.SHIBOKEN_LIBRARY_PATH.set("{root}/shiboken2")
