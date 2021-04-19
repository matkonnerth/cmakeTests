if(CONAN_EXPORTED)
# Conan is being used to build this package. Do not run it again!
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)
else()
include(/opt/conan-cmake/conan.cmake)
conan_cmake_run(
    CONANFILE conanfile.txt
    UPDATE
    BASIC_SETUP
    CMAKE_TARGETS
    BUILD never
    ARCH ${CMAKE_SYSTEM_PROCESSOR}
)
endif()

add_executable(testExe main.cpp)
target_link_libraries(testExe PRIVATE CONAN_PKG::outputWrapper)

