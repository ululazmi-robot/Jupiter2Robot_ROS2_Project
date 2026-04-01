import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    pkg_path = get_package_share_directory('jupiterobot2_description')
    pkg_gazebo = get_package_share_directory('gazebo_ros')

    xacro_file = os.path.join(pkg_path, 'urdf', 'jupiter2_pro.urdf.xacro')

    robot_description = Command([
        'xacro ',
        xacro_file
    ])

    return LaunchDescription([

        # Gazebo (replaces RViz2)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_gazebo, 'launch', 'gazebo.launch.py')
            )
        ),

        # Robot State Publisher (kept the same)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': robot_description,
                'use_sim_time': True   # changed False -> True for Gazebo
            }]
        ),

        # Spawn Entity (replaces joint_state_publisher_gui)
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'jupiter2',
                '-topic',  'robot_description',
                '-x', '0.0',
                '-y', '0.0',
                '-z', '0.1',
            ],
            output='screen'
        ),

    ])