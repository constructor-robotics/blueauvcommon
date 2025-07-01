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

    xrc_node = Node(
        package='bluerov2common',
        executable='xrcClientStart.sh',
        name='xrcClientStart',
        output='screen',
        parameters=[],
        arguments=[]
    )
    ld.add_action(xrc_node)

    pwm_node = Node(
        package='bluerov2common',
        executable='pwmServicesMaintube.py',
        name='pwmServices',
        output='screen',
        parameters=[],
        arguments=[]
    )
    ld.add_action(pwm_node)

    power_node = Node(
        package='bluerov2common',
        executable='powerControlBottomTube.py',
        name='powerControl',
        output='screen',
        parameters=[],
        arguments=[]
    )
    ld.add_action(power_node)

    # this starts the bottom tube
    bottom_tube_start = ExecuteProcess(
        cmd=['ros2', 'service', 'call', '/power_control_bottom_service',
             'bluerov2commonmsgs/srv/RestartSonarService',
             "tube_state: true"],
        output='screen'
    )
    ld.add_action(bottom_tube_start)



    return ld
