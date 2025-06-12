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

    # parameters_file_path = Path(get_package_share_directory('waterlinked_a50'), 'param', 'params.yaml')

    dvl_gzebo_node = Node(
        package='gazebo_px4',
        executable='my_custom_bridge',
        name='my_custom_bridge',
        output='screen',
        parameters=[],
        arguments=[]
    )
    ld.add_action(dvl_gzebo_node)

    foxglove_node = Node(
        package='foxglove_bridge',
        executable='foxglove_bridge',
        name='foxglove_bridge',
        parameters=[
            {'port': 8765},
            {'address': '0.0.0.0'},
            {'tls': False},
            {'certfile': ''},
            {'keyfile': ''},
            {'topic_whitelist': ['.*']},
            {'param_whitelist': ['.*']},
            {'service_whitelist': ['.*']},
            {'client_topic_whitelist': ['.*']},
            {'min_qos_depth': 1},
            {'max_qos_depth': 10},
            {'num_threads': 0},
            {'send_buffer_limit': 10000000},
            {'use_sim_time': False},
            {'capabilities': ['clientPublish', 'parameters', 'parametersSubscribe', 'services', 'connectionGraph', 'assets']},
            {'include_hidden': False},
            {'asset_uri_allowlist': ["^package://(?:[-\\w%]+/)*[-\\w%]+\\.(?:dae|fbx|glb|gltf|jpeg|jpg|mtl|obj|png|stl|tif|tiff|urdf|webp|xacro)$"]},
            {'ignore_unresponsive_param_nodes': True}
        ],
        output='screen'
    )
    ld.add_action(foxglove_node)


    return ld
