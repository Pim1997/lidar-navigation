# Lidar-navigation

## Description:
This github contains multiple packages which enable to navigate through a mapped environment with a Hokuyo UBG-04LX-F01 lidar. This lidar is placed in the middle of a Turtlebot 2. While launching the package it is possible to send 2D nav goals to the Turtlebot via RVIZ. The turtlebot will drive to the given goal using the lidar and the encoders of the turtlebot to know its movement.

## Prerequisites:
- Ros Kinetic on Ubuntu 16.04 or higher
- Hokuyo ubg-04lx-f01

## The packages:
### Laser_proc:
The laser_proc package is used to convert the representations of sensor_msgs/LaserScan and sensor_msgs/MultiEchoLaserScan.
### Lidar_navigation:
The lidar_navigation packages is made for making a map and opening a created map. The created maps can be placed in the directory "maps". There is a launch directory where the launchfiles for mapping and for driving through the mapped map are placed. The lidar_gmapping_navigation.launch in the launch directory is made for mapping. The lidar_amcl_navigation.launch is created to open the mapped map and open the other packages that are uesed for navigating through the map.
### Turtlebot_lidar_bringup:
This package is used to start up the turtlebot
### Turtlebot_lidar_description:
In this package are the specifications of the turtlebot defined. This package is added to our because the other packages link often to this package, so instead of changing every direction we added the package to our package.
### Turtlebot_lidar_navigation:
In this package all navigation parameters are defined. Like all costmap parameters and path planner parameters. These are defined in the directory "param". The parameters are standing in the .yaml files.
### Turtlebot_lidar_rviz_launchers:
This package is only used for opening RVIZ on your screen.
### Urg_c:
This urg_c is a libary for the urg_node.
### Urg_node:
The urg_node is a driver for Hokuyo lidar systems which makes it possible to use a Hokuyo sensor in ROS. In this driver the settings of the hokuyo lidar are defined. These can be configured in the "cfg" directory. 

## Installation:
