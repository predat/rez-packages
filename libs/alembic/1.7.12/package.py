# -*- coding: utf-8 -*-


name = "alembic"

version = "1.7.12"

authors = []

description = \
    """
    """

variants = [["platform-linux"]]

private_build_requires = [
    'gcc-6.3.1',
    'hdf5-1.10',
    'ilmbase-2.4',
    'boost-1.70'
]

requires = [
    'pyilmbase-2.4',
]

tools = []

uuid = "repository.alembic"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append('{root}/lib/python%s.%s/site-packages' % (
        env.REZ_PYTHON_MAJOR_VERSION,
        env.REZ_PYTHON_MINOR_VERSION))

    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")
