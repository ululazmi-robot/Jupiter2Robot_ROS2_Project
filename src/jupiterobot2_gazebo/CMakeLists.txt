cmake_minimum_required(VERSION 3.8)
project(jupiterobot2_gazebo)

################################################################################
# Compile options
################################################################################
add_compile_options(-std=c++17)

################################################################################
# Find dependencies
################################################################################
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(gazebo_ros REQUIRED)

################################################################################
# Install launch, models, rviz
################################################################################
install(
  DIRECTORY launch models rviz worlds
  DESTINATION share/${PROJECT_NAME}
)

################################################################################
# Export package
################################################################################
ament_package()

