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

    ekf_node = Node(
        package='bluerov2common',
        executable='ekfNode',
        name='ekfNode',
        output='screen',
        parameters=[
            {'simulation': False},
            {'dvl_position': [0.0,0.0,0.0]},
            {'dvl_rotation': [0.0,0.0,2.35619449019]},
            {'imu_position': [0.0,0.0,0.0]},
            {'imu_rotation': [0.0,0.0,3.14159265359]},
            {'baro_position': [0.0,0.0,0.0]}
        ],
        arguments=[]
    )
    ld.add_action(ekf_node)


    return ld
