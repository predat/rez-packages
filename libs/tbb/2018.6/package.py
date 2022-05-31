# -*- coding: utf-8 -*-

name = "tbb"

version = "2018.U6"

authors = [
    "Intel"
]

description = \
    """
    Threading Building Blocks is a C++ template library developed by Intel for parallel programming on multi-core
    processors. Using TBB, a computation is broken down into tasks that can run in parallel. The library manages
    and schedules threads to execute these tasks.
    """

requires = [
    "cmake-3+"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "tbb-{version}".format(version=str(version))

def commands():
    env.LIBRARY_PATH.prepend("{root}/lib/intel64/gcc4.7")
    env.LD_LIBRARY_PATH.prepend("{root}/lib/intel64/gcc4.7")
    env.MIC_LIBRARY_PATH.prepend("{root}/lib/intel64/gcc4.7")
    env.MIC_LD_LIBRARY_PATH.prepend("{root}/lib/intel64/gcc4.7")
    env.CPATH.prepend("{root}/include")
    env.TBBROOT.set("{root}")
    env.TBB_TARGET_ARCH.set("intel64")
    env.TBB_TARGET_PLATFORM.set("linux")

    # Helper environment variables.
    env.TBB_BINARY_PATH.set("{root}/bin")
    env.TBB_INCLUDE_PATH.set("{root}/include")
    env.TBB_LIBRARY_PATH.set("{root}/lib/" + str(env.TBB_TARGET_ARCH) + "/gcc4.7")
