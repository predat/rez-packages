set(glew_INCLUDE_DIRS $ENV{REZ_GLEW_ROOT}/include)
set(glew_LIBRARY_DIRS $ENV{REZ_GLEW_ROOT}/lib)
if(glew_STATIC)
    set(glew_LIBRARIES ${glew_LIBRARY_DIRS}/libGLEW.a)
else()
    set(glew_LIBRARIES ${glew_LIBRARY_DIRS}/libGLEW.so)
endif()

