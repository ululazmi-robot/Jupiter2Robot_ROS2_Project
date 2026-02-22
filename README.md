🤖 Jupiter2Robot ROS2 Platform

🚀 Overview

Jupiter2Robot is a modular ROS2-based robotic architecture developed for simulation, kinematic modeling, and autonomous system experimentation using Gazebo and RViz.

This project demonstrates:

-Multi-package ROS2 design

-Modular robot description (Arm + Head)

-Gazebo simulation integration

-Performance logging and system latency tracking

-Clean ROS2 workspace structure




🧱 System Architecture

The system consists of:

-Robot Description Layer (URDF/XACRO)

-Simulation Layer (Gazebo)

-Visualization Layer (RViz)

-Modular subsystem packages

-Performance logging module




🛠 Technologies Used

-ROS2 Humble

-Gazebo

-RViz

-URDF / Xacro

-colcon build system

-Ubuntu 22.04




⚙️ Build Instructions

colcon build

source install/setup.bash




🎮 Run Simulation

ros2 launch jupiterrobot2_gazebo gazebo.launch.py




📊 Performance Metrics

Latency analysis stored in:

latency_log.tsv





🧠 Engineering Concepts Demonstrated

-Modular robot modeling

-Simulation-based validation

-ROS2 package structuring

-Multi-node architecture

-Workspace isolation

-Build system management




🔮 Future Enhancements

-SLAM integration

-Navigation2 stack

-Autonomous task execution

-Sensor fusion

-Real hardware deployment





👨‍💻 Author

Ululazmi Sarif

Robotics & Autonomous Systems Developer
