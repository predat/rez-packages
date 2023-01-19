set(png_INCLUDE_DIRS $ENV{REZ_PNG_ROOT}/include)
set(png_LIBRARY_DIRS $ENV{REZ_PNG_ROOT}/lib64)
if(png_STATIC)
	set(png_LIBRARIES ${png_LIBRARY_DIRS}/libpng.a)
else()
	set(png_LIBRARIES ${png_LIBRARY_DIRS}/libpng.so)
endif()