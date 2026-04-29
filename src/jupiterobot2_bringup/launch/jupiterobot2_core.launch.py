import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Find the parameter file for the turtlebot3 base
    tb3_param_dir = LaunchConfiguration(
        'tb3_param_dir',
        default=os.path.join(
            get_package_share_directory('turtlebot3_bringup'),
            'param',
            'humble',
            'burger.yaml'))

    core_node = Node(
        package='turtlebot3_node',
        executable='turtlebot3_ros',
        name='turtlebot3_node',
        parameters=[
            tb3_param_dir, 
            {
                'namespace': '',
                'odometry.frame_id': 'odom',
                'odometry.child_frame_id': 'base_footprint',
                'odometry.publish_tf': True,
                'odometry.use_imu': True
            }
        ],
        arguments=['-i', '/dev/ttyACM0'],
        output='screen'
    )

    return LaunchDescription([core_node])