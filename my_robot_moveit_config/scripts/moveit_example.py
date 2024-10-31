#!/usr/bin/env python3
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

# Initialize moveit_commander and rospy
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

# Instantiate a RobotCommander, PlanningSceneInterface, and MoveGroupCommander
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("manipulator")

# Create a publisher for visualizing the planned path in Rviz
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=10)

# Define the pose target
pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.w = 1.0
pose_target.position.x = 0.3
pose_target.position.y = 0.0
pose_target.position.z = 1.1

# Set the target pose for the MoveGroupCommander
group.set_pose_target(pose_target)

# Plan the motion to the target pose
plan = group.plan()

# Executing the plan in simulation
group.go(wait=True)

# Allow some time for the planning process to finish
rospy.sleep(5)

# Shut down moveit_commander
moveit_commander.roscpp_shutdown()
