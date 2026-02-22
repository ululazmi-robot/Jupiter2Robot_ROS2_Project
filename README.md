🌍 Jupiter2Robot ROS2 Project
📌 Overview

Jupiter2Robot is a modular ROS2-based robotic system developed for simulation, visualization, and autonomous experimentation using Gazebo and RViz.

The project includes:

Robot Description (URDF/XACRO)

Arm and Head modules

Gazebo simulation environment

ROS2 integration

Performance logging

🛠 System Requirements

Ubuntu 22.04

ROS2 Humble

Gazebo

colcon build system

📂 Project Structure
Jupiter2Robot_ROS2_Project/
│
├── src/
│   ├── jupiterrobot2_description/
│   ├── jupiterrobot2_arm_description/
│   ├── jupiterrobot2_head_description/
│   └── jupiterrobot2_gazebo/
⚙️ Build Instructions
cd ~/Jupiter2Robot_ROS2_Project
colcon build
source install/setup.bash

🧠 Features

Modular robot design

Multi-package ROS2 architecture

Gazebo integration

Arm and head subsystems

Scalable for SLAM and navigation integration

👨‍💻 Author

Muhammad Ulul Azmi Bin Sarif
Robotics & ROS2 Developer