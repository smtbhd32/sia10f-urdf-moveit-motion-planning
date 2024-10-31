cmake_minimum_required(VERSION 3.0.2)
project(dependencies)

# Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  urdf
  robot_state_publisher
  joint_state_publisher
  gazebo_ros
  rviz
  xacro
)

# Declare the catkin package
catkin_package(
  #  INCLUDE_DIRS include
  #  LIBRARIES dependencies
  #  CATKIN_DEPENDS roscpp std_msgs
  #  DEPENDS system_lib
)

# Specify additional locations of header files
include_directories(
  ${catkin_INCLUDE_DIRS}
)

# If you have custom launch files, install them (optional)
install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
