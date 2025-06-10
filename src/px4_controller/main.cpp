/****************************************************************************
 * Copyright (c) 2024 PX4 Development Team.
 * SPDX-License-Identifier: BSD-3-Clause
 ****************************************************************************/

#include "rclcpp/rclcpp.hpp"

#include "mode.hpp"
#include <px4_ros2/components/node_with_mode.hpp>
#include "controllerOfBluerov2.h"
using MyNodeWithMode = px4_ros2::NodeWithMode<UUVAttModeTest>;


static const std::string kNodeName = "example_mode_uuv_attitude";
static const bool kEnableDebugOutput = true;

int main(int argc, char *argv[]) {
    rclcpp::init(argc, argv);

    auto nodePX4Shared = std::make_shared<MyNodeWithMode>(kNodeName, kEnableDebugOutput);
    auto nodeControllLogic = std::make_shared<controllerOfBluerov2>();
    rclcpp::executors::MultiThreadedExecutor executor;

    executor.add_node(nodePX4Shared);
    executor.add_node(nodeControllLogic);

    std::thread executor_thread(std::bind(&rclcpp::executors::MultiThreadedExecutor::spin, &executor));
    // rclcpp::spin(std::make_shared<MyNodeWithMode>(kNodeName, kEnableDebugOutput));
    rclcpp::shutdown();
    return 0;
}
