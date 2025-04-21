#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "RobotController.h"

namespace py = pybind11;

PYBIND11_MODULE(robot_bindings, m) {
    py::class_<RobotController>(m, "RobotController")
        .def(py::init<>())
        .def("moveForward", &RobotController::moveForward)
        .def("getStatus", &RobotController::getStatus);
}