#include "RobotController.h"

RobotController::RobotController() : status_("Idle") {}

std::string RobotController::moveForward(double speed)
{
    if (speed > 0)
    {
        status_ = "Moving forward";
    }
    else
    {
        status_ = "Stopped";
    }
    return status_;
}

std::string RobotController::getStatus() const
{
    return status_;
}
