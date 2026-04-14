import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # 1. Paths to your configuration files
    pkg_gazebo = get_package_share_directory('jupiterobot2_gazebo')
    
    # Path to your No-Odom SLAM params
    config_file = os.path.join(pkg_gazebo, 'config', 'mapper_params_no_odom.yaml')
    
    # Path to your RViz config (Make sure this file exists in your rviz folder)
    rviz_config_path = os.path.join(pkg_gazebo, 'rviz', 'slam_toolbox.rviz')

    # 2. Slam Toolbox Node (No-Odom)
    slam_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[
            config_file, 
            {'use_sim_time': True}
        ]
    )

    # 3. RViz2 Node
    # It will use your config file if found; otherwise, it opens a blank RViz
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_path] if os.path.exists(rviz_config_path) else [],
        output='screen',
        parameters=[{'use_sim_time': True}]
    )

    # 4. Return Launch Description
    return LaunchDescription([
        slam_node,
        rviz_node
    ])