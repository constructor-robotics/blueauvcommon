from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable, ExecuteProcess

from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from pathlib import Path

def generate_launch_description():

    ld = LaunchDescription()

    # Set env var to print messages to stdout immediately
    arg = SetEnvironmentVariable('RCUTILS_CONSOLE_STDOUT_LINE_BUFFERED', '1')
    ld.add_action(arg)


    pwm_node = Node(
        package='bluerov2common',
        executable='pwmServicesSensortube.py',
        name='pwmServices',
        output='screen',
        parameters=[],
        arguments=[]
    )
    ld.add_action(pwm_node)


    baro_node = Node(
        package='bluerov2common',
        executable='barometer_node',
        name='barometer_sensor_tube',
        output='screen',
        parameters=[],
        arguments=[]
    )
    ld.add_action(baro_node)



    return ld
