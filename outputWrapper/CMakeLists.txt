
if(CONAN_EXPORTED)
# Conan is being used to build this package. Do not run it again!
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)
else()
include(/opt/conan-cmake/conan.cmake)
conan_cmake_run(
    CONANFILE conanfile.py
    UPDATE
    BASIC_SETUP
    CMAKE_TARGETS
    BUILD never
    ARCH ${CMAKE_SYSTEM_PROCESSOR}
)
endif()

add_library(outputWrapper SHARED src/outputWrapper.cpp)
target_include_directories(outputWrapper PUBLIC ${CMAKE_CURRENT_LIST_DIR}/include)
target_link_libraries(outputWrapper PRIVATE CONAN_PKG::output)
