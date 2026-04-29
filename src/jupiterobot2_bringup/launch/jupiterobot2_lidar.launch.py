from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rplidar_ros',
            executable='rplidar_node',
            name='rplidar_node',
            parameters=[{
                'channel_type': 'serial',
                'serial_port': '/dev/ttyUSB1', # Ensure this matches your port
                'serial_baudrate': 115200,     # Match your ROS 1 config
                'frame_id': 'base_scan',
                'inverted': False,
                'angle_compensate': True,
            }],
            output='screen'
        )
    ])