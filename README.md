### Motoman SIA10F Simulation with MoveIt!

#### Project Description
This project simulates the Motoman SIA10F robotic arm using the MoveIt! package in ROS1. It provides a step-by-step approach to creating URDF files, configuring MoveIt packages, and performing motion planning with Python. This resource aims to help developers understand and implement robotic arm functionalities in a Gazebo simulation.

#### Key Features
- **URDF model of the Motoman SIA10F robot arm.**
- **MoveIt! integration for motion planning and execution.**
- **RViz visualization with configurable settings.**
- **Python scripts for planning and controlling the arm:** Added scripts for commanding the robotic arm directly via Python.

#### Installation Instructions

##### Prerequisites
- **ROS Noetic:** Ensure it’s installed and configured with a Catkin workspace.

##### Setup
1. **Clone the repository into your Catkin workspace:**
    ```bash
    cd ~/ros_ws/src
    git clone https://github.com/smtbhd32/sia10f-urdf-moveit-motion-planning.git
    ```

2. **Install Dependencies:** Use `rosdep` to install all dependencies listed in the `package.xml`:
    ```bash
    cd ~/ros_ws
    rosdep install --from-paths src --ignore-src -r -y
    ```

3. **Build the Workspace:**
    ```bash
    catkin_make
    ```

4. **Source the Workspace:**
    ```bash
    source devel/setup.bash
    ```

#### Usage
- **Run the main simulation launch file:**
    ```bash
    roslaunch sia10f_gazebo main.launch
    ```

##### Running MoveIt for Motion Planning
- **To control the robot arm with MoveIt and RViz:**
    ```bash
    roslaunch my_robot_moveit_config my_robot_planning_execution.launch
    ```

##### Running Python Control Scripts
The `scripts` folder contains Python scripts for commanding the robot arm through MoveIt.

1. **Navigate to the scripts folder:**
    ```bash
    cd ~/ros_ws/src/sia10f_robot/my_robot_moveit_config/scripts
    ```

2. **Run the example script:**
    ```bash
    rosrun my_robot_moveit_config moveit_joint_control_example.py
    ```
    This script sets joint values for the "manipulator" group and executes the plan.

#### Folder Structure
- **sia10f_control:** Control configurations and launch files.
- **sia10f_description:** URDF and Xacro files defining the robot’s model.
- **sia10f_gazebo:** Gazebo simulation files.
- **my_robot_moveit_config:** MoveIt! configurations for the SIA10F robot.
- **scripts:** Contains Python scripts for planning and executing commands via MoveIt.

#### Acknowledgements
This project builds upon tutorials by The Construct and resources from other contributors.

---
