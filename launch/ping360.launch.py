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


    ping_360_node = Node(
        package='ping360_sonar',
        executable='ping360_node',
        name='ping360_node',
        output='screen',
        parameters=[{"device": "/dev/ping360"},
                    {"baudrate": 115200},
                    {"gain": 0},
                    {"numberOfSamples": 500},
                    {"transmitFrequency": 750},
                    {"sonarRange": 20},
                    {"speedOfSound": 1500},
                    {"debug": False},
                    {"threshold": 200},
                    {"enableDataTopic": True},
                    {"maxAngle": 400},
                    {"minAngle": 0},
                    {"oscillate": True},
                    {"step": 1},
                    {"imgSize": 500},
                    {"queueSize": 1}
                    ],
        arguments=[]
    )
    ld.add_action(ping_360_node)

    return ld
