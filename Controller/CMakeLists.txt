add_library(robot_controller
    src/RobotController.cpp
)

target_include_directories(robot_controller PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
