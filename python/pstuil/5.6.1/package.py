name = "psutil"

version = "5.6.1"

authors = ["Giampaolo Rodola"]

description = \
    """
psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. It is useful mainly for system monitoring, profiling and limiting process resources and management of running processes. It implements many functionalities offered by UNIX command line tools such as: ps, top, lsof, netstat, ifconfig, who, df, kill, free, nice, ionice, iostat, iotop, uptime, pidof, tty, taskset, pmap.
    """

build_requires = ["setuptools", "pip"]

variants = [
    ["platform-linux", "python-2.7"],
    ["platform-linux", "python-3"],

]

tools = [""]

uuid = "repository.psutil"

def commands():
    env.PYTHONPATH.append("{root}/python")
