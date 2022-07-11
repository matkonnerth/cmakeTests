set(CMAKE_VERBOSE_MAKEFILE ON)

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
# The LD linker complains even about missing link of transitive dependencies,
# altough they are private and hidden (wrapper library)
# LD needs to see them. This would require for consumer to have find_package
# in cmake for transitive and private dependencies.
# which is not what we want. We can fix this with this workaround
target_link_options(outputWrapper PUBLIC "-Wl,--unresolved-symbols=ignore-in-shared-libs")

enable_testing()
add_subdirectory(tests)
