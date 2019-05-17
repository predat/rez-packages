name = 'build'
version = 'release'

build_command = False

def commands():
    env.CMAKE_BUILD_TYPE = 'RELEASE'

