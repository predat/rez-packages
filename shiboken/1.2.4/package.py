name = "shiboken"

version = "1.2.4"

authors = [
    "pyside"
]

description = \
    """
    Python bindings generator that uses API Extractor and outputs CPython code.
    """

requires = [
    "qt",
    "python-2.7"
]

build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

uuid = "repository.shiboken"

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append('{root}/lib64/python2.7/site-packages')

    if building:
        env.SHIBOKEN_INCLUDE_DIR.append('{root}/include')
