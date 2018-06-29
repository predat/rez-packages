set(glfw_INCLUDE_DIRS $ENV{REZ_GLFW_ROOT}/include)
set(glfw_LIBRARY_DIRS $ENV{REZ_GLFW_ROOT}/lib)
if(glfw_STATIC)
    set(glfw_LIBRARIES ${glfw_LIBRARY_DIRS}/libglfw3.a)
else()
    set(glfw_LIBRARIES ${glfw_LIBRARY_DIRS}/libglfw..so)

