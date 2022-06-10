# Taken from OSS-Pipeline form https://github.com/OSS-Pipeline/rez-pyside2

name = "pyside2"

version = "5.12.5.py2"

authors = [
    "The Qt Company"
]

description = \
    """
    The Qt for Python project aims to provide a complete port of the PySide module to Qt 5.
    """

requires = [
    "cmake-3+",
    "python-2.7+<3",
    "shiboken2-{version}".format(version=str(version))
]

variants = [
    ["platform-linux"]
]

tools = [
    "pyside2-lupdate",
    "pyside2-rcc",
    "pyside2-uic"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "pyside2-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}")

    # Helper environment variables.
    env.PYSIDE_BINARY_PATH.set("{root}/bin")
    env.PYSIDE_INCLUDE_PATH.set("{root}/PySide2/include")
    env.PYSIDE_LIBRARY_PATH.set("{root}/PySide2")
