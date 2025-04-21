#ifndef ROBOT_CONTROLLER_H
#define ROBOT_CONTROLLER_H

#include <string>

class RobotController
{
public:
    RobotController();

    std::string moveForward(double speed);
    std::string getStatus() const;

private:
    std::string status_;
};

#endif // ROBOT_CONTROLLER_H
