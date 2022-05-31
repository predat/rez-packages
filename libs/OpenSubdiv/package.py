#Taken from OSS-Pipeline and adjusted from 3.4.3 from https://github.com/OSS-Pipeline/rez-opensubdiv

name = "opensubdiv"

version = "3.4.4"

authors = [
    "Pixar"
]

description = \
    """
    OpenSubdiv is a set of open source libraries that implement high performance subdivision surface (subdiv)
    evaluation on massively parallel CPU and GPU architectures.
    """

requires = [
    "cmake-3+",
    "doxygen-1.8+",
    "gcc-6+",
    "glfw-3+",
    "ptex-2.1.28+",
    "python-2.7+<3",
    "tbb-2017.U6+",
    "zlib-1.2+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "far_perf",
    "far_regression",
    "farViewer",
    "glEvalLimitv",
    "glFVarViewer",
    "glImaging",
    "glPaintTest",
    "glPtexViewer",
    "glShareTopology",
    "glStencilViewer",
    "glViewer",
    "hbr_baseline",
    "hbr_regression",
    "osd_regression",
    "stringify"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "opensubdiv-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    # Helper environment variables.
    env.OPENSUBDIV_BINARY_PATH.set("{root}/bin")
    env.OPENSUBDIV_INCLUDE_PATH.set("{root}/include")
    env.OPENSUBDIV_LIBRARY_PATH.set("{root}/lib")

