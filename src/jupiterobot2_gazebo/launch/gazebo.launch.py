import os
from os import pathsep
from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory, get_package_prefix

def generate_launch_description():

    # --------------------
    # Set GAZEBO_MODEL_PATH so all mesh packages are found
    # --------------------
    desc_share  = get_package_share_directory("jupiterobot2_description")
    desc_prefix = get_package_prefix("jupiterobot2_description")

    model_path  = os.path.join(desc_share, "models")
    model_path += pathsep + os.path.join(desc_prefix, "share")

    # Add head description package if it exists
    try:
        head_prefix = get_package_prefix("jupiterobot2_head_description")
        model_path += pathsep + os.path.join(head_prefix, "share")
    except Exception:
        pass  

    # Add arm description package to fix the missing mesh errors
    try:
        arm_prefix = get_package_prefix("jupiterobot2_arm_description")
        model_path += pathsep + os.path.join(arm_prefix, "share")
    except Exception:
        pass

    env_var = SetEnvironmentVariable("GAZEBO_MODEL_PATH", model_path)
    
    # --------------------
    # Prevent Gazebo from hanging on the dead model database
    # --------------------
    env_var_uri = SetEnvironmentVariable("GAZEBO_MODEL_DATABASE_URI", "")

    # --------------------
    # Robot description
    # --------------------
    robot_description = Command([
        'xacro ',
        PathJoinSubstitution([
            FindPackageShare('jupiterobot2_description'),
            'urdf',
            'jupiter2_pro.urdf.xacro'
        ])
    ])

    # --------------------
    # Gazebo
    # --------------------
    gazebo = ExecuteProcess(
        cmd=[
            'gazebo',
            '--verbose',
            '-s', 'libgazebo_ros_init.so',
            '-s', 'libgazebo_ros_factory.so'
        ],
        output='screen'
    )

    # --------------------
    # Robot state publisher
    # --------------------
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': True
        }]
    )

    # --------------------
    # Spawn entity
    # --------------------
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'jupiter2',
            '-timeout', '60'
        ],
        output='screen'
    )

    return LaunchDescription([
        env_var,          
        env_var_uri,      
        gazebo,
        robot_state_publisher,
        spawn_entity
    ])
