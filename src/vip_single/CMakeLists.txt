cmake_minimum_required(VERSION 3.8)
project(vip_single)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav2_msgs REQUIRED)

install(PROGRAMS
  scripts/vip_manager_simulation.py
  scripts/vip_manager_hardware.py
  scripts/vip_manager_hardware_spare.py
  scripts/vip_manager_hardware_demo.py
  scripts/vip_manager_hardware_move.py
  scripts/vip_manager_hardware_basic_move.py
  scripts/vip_manager_sound_player_node.py
  scripts/demo_fcoee_1.py
  DESTINATION lib/${PROJECT_NAME}
)

# Important for later use
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
  DESTINATION share/${PROJECT_NAME}/sounds
)

ament_package()