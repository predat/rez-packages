CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)

#FILE(GLOB_RECURSE python_libs "install_deps/python/lib")
#rez_install_files(
#  ${python_libs}
#  DESTINATION .
#)

FILE(GLOB_RECURSE bin "install_deps/bin/*.sh")
rez_install_files(
  ${bin}
  RELATIVE install_deps/bin
  DESTINATION bin
  EXECUTABLE
)

FILE(GLOB_RECURSE etc "install_deps/etc/*")
rez_install_files(
  ${etc}
  RELATIVE install_deps/etc
  DESTINATION etc
)

FILE(GLOB_RECURSE share "install_deps/share/*")
rez_install_files(
  ${share}
  RELATIVE install_deps/share
  DESTINATION share
)
