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
                'serial_port': '/dev/ttyUSB1',  # <-- Fixed port to USB0
                'serial_baudrate': 115200,      
                'frame_id': 'base_scan',
                'inverted': False,
                'angle_compensate': True,
                'scan_mode': 'Sensitivity',     # <-- Added to prevent buffer overflow
            }],
            output='screen'
        )
    ])