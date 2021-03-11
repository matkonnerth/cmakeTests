#if(CONAN_EXPORTED)
## Conan is being used to build this package. Do not run it again!
#include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
#conan_basic_setup(TARGETS)
#else()
#include(/opt/conan-cmake/conan.cmake)
#conan_cmake_run(
#    CONANFILE conanfile.txt
#    UPDATE
#    BASIC_SETUP
#    CMAKE_TARGETS
#    BUILD never
#    ARCH ${CMAKE_SYSTEM_PROCESSOR}
#)
#endif()
include(CTest)
add_executable(testExe testExe.cpp)
target_link_libraries(testExe PRIVATE outputWrapper)
add_test(testExe ${CMAKE_BINARY_DIR}/bin/testExe)

