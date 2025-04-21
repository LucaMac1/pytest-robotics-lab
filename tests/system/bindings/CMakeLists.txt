find_package(pybind11 REQUIRED)

pybind11_add_module(robot_bindings robot_bindings.cpp)
target_include_directories(robot_bindings PRIVATE
    ${PROJECT_SOURCE_DIR}/Controller/include
)
target_link_libraries(robot_bindings PRIVATE robot_controller)