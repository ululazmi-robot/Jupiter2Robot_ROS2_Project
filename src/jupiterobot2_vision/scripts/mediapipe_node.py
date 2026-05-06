#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MediaPipeNode(Node):
    def __init__(self):
        super().__init__('mediapipe_node')
        self.get_logger().info("MediaPipe Node Started")

def main(args=None):
    rclpy.init(args=args)
    node = MediaPipeNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()