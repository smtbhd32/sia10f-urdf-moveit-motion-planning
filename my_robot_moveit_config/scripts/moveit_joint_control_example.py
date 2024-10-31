#!/usr/bin/env python3

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

# Initialize the moveit_commander and rospy node
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

# Instantiate RobotCommander (interface to the robot), PlanningSceneInterface (environment), and MoveGroupCommander (controls a planning group)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("manipulator")

# Create a DisplayTrajectory publisher, which publishes display trajectories to RViz
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

# Get the current joint values and modify them for the new target
group_variable_values = group.get_current_joint_values()
group_variable_values[3] = 1.5
group.set_joint_value_target(group_variable_values)

# Plan to the joint-space goal and execute the plan
plan2 = group.plan()
group.go(wait=True)

# Give some time for the plan to execute
rospy.sleep(5)

# Shutdown the moveit_commander
moveit_commander.roscpp_shutdown()
