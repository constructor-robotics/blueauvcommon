/****************************************************************************
 * Copyright (c) 2023 PX4 Development Team.
 * SPDX-License-Identifier: BSD-3-Clause
 ****************************************************************************/
#pragma once

#include <cmath>

#include <px4_ros2/components/mode.hpp>
#include <px4_ros2/control/setpoint_types/experimental/attitude.hpp>

#include <rclcpp/rclcpp.hpp>
#include "controllerOfBluerov2.h"
static const std::string kName = "uuv attitude Example";

class UUVAttModeTest : public px4_ros2::ModeBase
{
public:
  explicit UUVAttModeTest(rclcpp::Node & node)
  : ModeBase(node, kName),controller_(nullptr)
  {
    this->_att_setpoint = std::make_shared<px4_ros2::AttitudeSetpointType>(*this);
  }

  void setController(std::shared_ptr<controllerOfBluerov2> controller) {
    this->controller_ = controller;
  }

  void onActivate() override {}

  void onDeactivate() override {}

  void updateSetpoint(float dt_s) override
  {
    // Setting constant angles and thrust.
    // _att_setpoint->update(-0.0f * M_PI / 180.f, 0.0f * M_PI / 180.f, 20.0f * M_PI / 180.f, {0.5f, 0.f, 0.f});

    this->controller_->getRollPitchYawThrustControllLogic(this->des_thrust,this->des_rpy);

    this->_att_setpoint->update(static_cast<float>(des_rpy[0]), static_cast<float>(des_rpy[1]), static_cast<float>(des_rpy[2]),
      {static_cast<float>(des_thrust.x()), static_cast<float>(des_thrust.y()),static_cast<float>(des_thrust.z())});

  }

private:
  std::shared_ptr<px4_ros2::AttitudeSetpointType> _att_setpoint;
  std::shared_ptr<controllerOfBluerov2> controller_;

  Eigen::Vector3d des_thrust;
  Eigen::Vector3d des_rpy;
};
