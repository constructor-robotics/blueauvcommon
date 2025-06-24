from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from pathlib import Path

def generate_launch_description():

    ld = LaunchDescription()

    # Set env var to print messages to stdout immediately
    arg = SetEnvironmentVariable('RCUTILS_CONSOLE_STDOUT_LINE_BUFFERED', '1')
    ld.add_action(arg)

    waterlinked_node = Node(
        package='waterlinked_a50',
        executable='dvl_node',
        name='dvl_node',
        output='screen',
        parameters=[{"IP": "192.168.10.12"},
                    {"port": "16171"},
                    {"dvl_pos_topic_name": "position_estimate"},
                    {"dvl_vel_topic_name": "velocity_estimate"}
                    ],
        arguments=[]
    )
    ld.add_action(waterlinked_node)

    return ld
