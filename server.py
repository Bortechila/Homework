#!/usr/bin/env python3

from first_pkg.srv import VelCommand 
from geometry_msgs.msg import Twist
import rospy


vel = Twist()
def cmd_vel_func():
    vel.linear.x = 0.2 
    vel.angular.z = 0.1
    pub.publish(vel)

def vel_command_handler(req):
    global vel
    vel.linear.x = req.x
    vel.angular.z = req.z
    return True


rospy.Service("vel_commander", VelCommand, vel_command_handler)

if __name__ == "__main__":
    rospy.init_node("server", anonymous= True)
    r = rospy.Rate(1)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size= 10)
    while not rospy.is_shutdown():
        cmd_vel_func()
    r.sleep()
