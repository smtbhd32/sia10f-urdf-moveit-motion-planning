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

### Setup Steps
1. Clone this repository into your ROS workspace:
   ```bash
   cd ~/ros_ws/src
   git clone https://github.com/smtbhd32/sia10f-urdf-moveit-motion-planning/
   ```

2. **Pull the latest changes** (if needed):
   ```bash
   cd sia10f-urdf-moveit-motion-planning
   git pull
   cd ..
   ```

3. Install all required packages and dependencies defined in the `rosdep` file:
   ```bash
   rosdep install --from-paths src --ignore-src -r -y
   ```

4. Build your workspace:
   ```bash
   cd ~/ros_ws
   catkin_make
   ```

5. Source the workspace:
   ```bash
   source devel/setup.bash
   ```

## Usage

### Launching the Robot Simulation
To launch the Gazebo simulation, use the following command:
```bash
roslaunch sia10f_gazebo main.launch
```

### Running MoveIt! for Planning and Execution
To control the robot using MoveIt!, launch the following command:
```bash
roslaunch my_robot_moveit_config my_robot_planning_execution.launch
```

### Example Commands
- View the Robot in RViz: Ensure that you have RViz installed, and launch the robot as specified above.

## Documentation
For additional resources and detailed explanations of the code, refer to the comments in the codebase and the configuration files.

## Acknowledgements
This project is based on the tutorial by The Construct (https://www.youtube.com/watch?v=J6Mu1P6FlxY). Special thanks for the valuable guidance in understanding ROS and robot simulation.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---
