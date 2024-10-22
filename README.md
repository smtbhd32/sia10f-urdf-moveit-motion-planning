# Motoman SIA10F Simulation with MoveIt!

## Project Description
This project focuses on simulating the Motoman SIA10F robotic arm using the MoveIt! package in ROS1. It serves as a basic tutorial for creating URDF files, building MoveIt packages, and performing motion planning through Python. The goal is to understand and implement robotic arm functionalities and provide a documented workflow for others to follow.

## Key Features
- Creation of a URDF file for the Motoman SIA10F robot arm.
- Integration with the MoveIt! package for motion planning.
- Visualization of the robot model in RViz.
- Configurable RViz settings for better visualization and debugging.

## Installation Instructions

### Prerequisites
- **ROS**: Ensure you have ROS Noetic installed on your system.
- **Catkin**: Make sure your ROS environment is set up with a Catkin workspace.

### Installing Required Packages

1. **Install Xacro**: Xacro is used for processing XACRO files.
   ```bash
   sudo apt-get install ros-noetic-xacro
   ```

2. **Install RViz**: RViz is required for visualizing the robot model.
   ```bash
   sudo apt-get install ros-noetic-rviz
   ```

3. **Install MoveIt!**: MoveIt! is used for motion planning and manipulation.
   ```bash
   sudo apt-get install ros-noetic-moveit
   ```

4. **Install Joint State Publisher**: The Joint State Publisher publishes the state of the robot's joints.
   ```bash
   sudo apt-get install ros-noetic-joint-state-publisher
   ```

5. **Install Robot State Publisher**: The Robot State Publisher publishes the state of the robot in TF.
   ```bash
   sudo apt-get install ros-noetic-robot-state-publisher
   ```

6. **Install Gazebo and Other Required Packages**: This command installs Gazebo and other necessary packages.
   ```bash
   sudo apt-get install ros-noetic-gazebo-ros ros-noetic-std-msgs ros-noetic-urdf ros-noetic-roscpp
   ```

### Setup Steps
1. Clone this repository into your ROS workspace:
   ```
   cd ~/ros_ws/src
   git clone https://github.com/smtbhd32/sia10f-urdf-moveit-motion-planning/
   ```

2. Build your workspace:
   ```
   cd ~/ros_ws
   catkin_make
   ```

3. Source the workspace:
   ```
   source devel/setup.bash
   ```

## Usage

### Launching the Robot
To launch the robot model in RViz, use the following command:
```
roslaunch my_robot_description my_robot.launch
```

### Example Commands
- View the Robot in RViz: Ensure that you have RViz installed, and launch the robot as specified above.

## Documentation
For additional resources and detailed explanations of the code, refer to the comments in the codebase and the configuration files.

## Acknowledgements
This project is based on the tutorial by The Construct (https://www.youtube.com/watch?v=J6Mu1P6FlxY). Special thanks for the valuable guidance in understanding ROS and robot simulation.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
