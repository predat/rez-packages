# From the OpenColorIO repository.

project(tinyxml)

cmake_minimum_required(VERSION 2.8)

add_library(tinyxml
    tinystr.cpp
    tinyxml.cpp
    tinyxmlerror.cpp
    tinyxmlparser.cpp)

set(TINYXML_COMPILE_FLAGS "-DTIXML_USE_STL")

if(UNIX)
    set(TINYXML_COMPILE_FLAGS "${TINYXML_COMPILE_FLAGS} -fPIC -fvisibility=hidden")
endif()

if(OCIO_INLINES_HIDDEN AND UNIX)
    set(TINYXML_COMPILE_FLAGS "${TINYXML_COMPILE_FLAGS} -fvisibility-inlines-hidden")
endif()

set_target_properties(tinyxml PROPERTIES
    COMPILE_FLAGS "${TINYXML_COMPILE_FLAGS}")

install(TARGETS
    tinyxml
    DESTINATION ${CMAKE_INSTALL_PREFIX}/lib)
install(FILES
    tinyxml.h tinystr.h
    DESTINATION ${CMAKE_INSTALL_PREFIX}/include)
