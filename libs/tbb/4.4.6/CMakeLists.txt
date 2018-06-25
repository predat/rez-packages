CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(tbb_version ${TBB_VERSION})
set(url_tbb https://github.com/01org/tbb/archive/${tbb_version}.tar.gz)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=on)


ExternalProject_add(
    tbb
    URL ${url_tbb}
    PREFIX tbb
    CONFIGURE_COMMAND ""
    INSTALL_COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/copy_files.sh ${CMAKE_CURRENT_BINARY_DIR}/tbb/src/tbb ${CMAKE_INSTALL_PREFIX}
    ALWAYS 1
    BUILD_IN_SOURCE 1
)

#ExternalProject_Get_Property(tbb source_dir)
#message(STATUS "tbb_source: ${source_dir}")
#file(GLOB_RECURSE libs ${source_dir}/build/*_release/libtbb*)
#install(FILES ${libs} DESTINATION lib)
#install(DIRECTORY ${source_dir}/include/serial DESTINATION include)
#install(DIRECTORY ${source_dir}/include/tbb DESTINATION include)


install(
    FILES cmake/tbb.cmake
    DESTINATION cmake
)
