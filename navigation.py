#!/usr/bin/env python  
import rospy
import argparse
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import *

#get location from user
parser = argparse.ArgumentParser(description='Goal_position')
parser.add_argument('goal_position', metavar='goal_position', type=str)
args = parser.parse_args()
goal_pose = args.goal_position

#declare goal_points:
goal_A = 2.3, 0.5
goal_B = 1.9, 5.1
goal_C = -0.5, 2.2
goal_D = -0.1, 5.5
goal_E = -3, 5.9
goal_F = -2.5, 3.7
goal_G = -3, -0.3
goal_H = -0.3, -0.7

def moveto_point(go_point):

   move_point = actionlib.SimpleActionClient("move_base", MoveBaseAction)
   while(not move_point.wait_for_server(rospy.Duration.from_sec(5.0))):
           rospy.loginfo("Waiting for the move_base action server to come up")
   goal = MoveBaseGoal() 
   goal.target_pose.header.frame_id = "map"
   goal.target_pose.header.stamp = rospy.Time.now()
   #goal position
   goal.target_pose.pose.position.x, goal.target_pose.pose.position.y = go_point
   goal.target_pose.pose.position.z = 0
   goal.target_pose.pose.orientation.x = 0.0
   goal.target_pose.pose.orientation.y = 0.0
   goal.target_pose.pose.orientation.z = 0.0
   goal.target_pose.pose.orientation.w = 1.0

   rospy.loginfo("Sending goal position ...")
   move_point.send_goal(goal)

   move_point.wait_for_result(rospy.Duration(60))

   if(move_point.get_state() ==  GoalStatus.SUCCEEDED):
           rospy.loginfo("Reached the destination")
           return True

   else:
           rospy.loginfo("Failed to reach the destination")
           return False


if __name__ == '__main__':
   
     rospy.init_node('map_navigation_1', anonymous=False)

     if goal_pose == "goal_A":
         print('started to goal')
         moveto_point(goal_A)
         #rospy.spin()
     elif goal_pose == 'goal_B':
        print('started to goal')
        moveto_point(goal_B)
        #rospy.spin()
     elif goal_pose == 'goal_C':
        print('started to goal')
        moveto_point(goal_C)
        #rospy.spin()
     elif goal_pose == 'goal_D':
        print('started to goal')
        moveto_point(goal_D)
        #rospy.spin()
     elif goal_pose == 'goal_E':
        print('started to goal')
        moveto_point(goal_E)
        #rospy.spin()
     elif goal_pose == 'goal_F':
        print('started to goal')
        moveto_point(goal_F)
        #rospy.spin()
     elif goal_pose == 'goal_G':
        print('started to goal')
        moveto_point(goal_G)
        #rospy.spin()
     elif goal_pose == 'goal_H':
        print('started to goal')
        moveto_point(goal_H)
        #rospy.spin()
     else:
         print("Goal location doesn't match")
