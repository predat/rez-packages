name = 'pip'

version = '9.0.1'

tools = [
    'pip',
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

requires = [
    'setuptools',
    'python-2.7'
]

build_requires = []

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = '2c43d523-92bb-4f2b-b812-70202f54d3f1'
