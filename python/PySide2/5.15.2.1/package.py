# -*- coding: utf-8 -*-

name = "pyside2"

version = "5.15.2.1"

requires = ["qt-5.15.8"]

private_build_requires = [
    "setuptools-41+",
    "cmake-3",
    "gxx-6+<10",
    "llvm-15",
    "git-2.26+",
    "wheel",
    "packaging",
    "python-3.7",
    "openssl-3"
]

variants = [
    ["platform-linux", "python-3"],
]

tools = [
    "rcc",
    "uic",
    "pyside2-uic",
    "shiboken2",
    "designer",
    "pyside_tool.py"
]

description = "Python bindings for the Qt cross-platform application and UI framework"

uuid = "repository.%s" % name


def commands():
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')

    # rez 2.0.0 does not provide '_MAJOR_VERSION' env var
    # env.PYTHONPATH.append('{root}/lib64/python%s.%s/site-packages' % (
    #     env.REZ_PYTHON_MAJOR_VERSION,
    #     env.REZ_PYTHON_MINOR_VERSION))
    # env.PYTHONPATH.append('{root}/lib/python%s/site-packages' % '.'.join(
    #     str(env.REZ_PYTHON_VERSION).split('.')[0:2]))
    env.PYTHONPATH.append('{root}/python')

    if building:
        env.CMAKE_PREFIX_PATH.append('{root}')
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')
