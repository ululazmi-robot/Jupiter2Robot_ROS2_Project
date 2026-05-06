#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import torch # To check for GPU
from ultralytics import YOLO

class YoloNode(Node):
    def __init__(self):
        super().__init__('yolo_node')
        
        # 1. Initialize Tools
        self.bridge = CvBridge()
        
        # 2. Load YOLOv8 Model
        # This will download 'yolov8n.pt' automatically on first run
        self.model = YOLO('yolov8n.pt') 
        
        # Check for NVIDIA GPU (TUF Gaming laptop)
        if torch.cuda.is_available():
            self.model.to('cuda')
            self.get_logger().info("Using NVIDIA GPU (CUDA) for YOLOv8")
        else:
            self.get_logger().info("Using CPU for YOLOv8")
        
        # 3. Subscriber: Listen to your laptop camera node
        self.subscription = self.create_subscription(
            Image,
            '/image_raw',  # Matches your ros2 topic list
            self.image_callback,
            10)
            
        # 4. Publisher: Send the annotated image to rqt
        self.publisher = self.create_publisher(Image, '/yolo_result', 10)
        
        self.get_logger().info("YOLOv8 Detection Node is Ready.")

    def image_callback(self, msg):
        try:
            # A. Convert ROS Image message to OpenCV format
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            
            # B. Run Inference
            # stream=True is more memory efficient for video
            results = self.model(cv_image, conf=0.5, verbose=False)
            
            # C. Visualize Results on the frame
            # results[0].plot() draws boxes, labels, and confidence scores
            annotated_frame = results[0].plot()
            
            # D. Convert back to ROS message and Publish
            result_msg = self.bridge.cv2_to_imgmsg(annotated_frame, encoding='bgr8')
            self.publisher.publish(result_msg)
            
        except Exception as e:
            self.get_logger().error(f"Detection Error: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = YoloNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down YOLOv8 Node...")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()