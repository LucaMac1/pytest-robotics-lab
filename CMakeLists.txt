cmake_minimum_required(VERSION 3.13)
project(RobotProject)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(pybind11 REQUIRED)

option(BUILD_PYBINDINGS "Build Python bindings using pybind11" OFF)

add_subdirectory(Controller)

if (BUILD_PYBINDINGS)
    add_subdirectory(tests/system/bindings)
endif()