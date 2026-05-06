cmake_minimum_required(VERSION 3.8)
project(vip_single)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav2_msgs REQUIRED)

install(PROGRAMS
  scripts/vip_manager.py
  DESTINATION lib/${PROJECT_NAME}
)

# Important for later use
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()