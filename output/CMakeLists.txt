add_library(output SHARED src/output.c)
target_include_directories(output PUBLIC ${CMAKE_CURRENT_LIST_DIR}/include)