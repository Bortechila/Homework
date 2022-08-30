#!/usr/bin/env python3

from first_pkg.srv import VelCommand 
from geometry_msgs.msg import Twist
import rospy


vel = Twist()
vel.linear.x = 0.35
vel.angular.z = 0
    

def vel_command_handler(req):
    vel.linear.x = req.x
    vel.angular.z = req.z
    return True


s = rospy.Service("vel_commander", VelCommand, vel_command_handler)

if __name__ == "__main__":
    rospy.init_node("server", anonymous= True)
    r = rospy.Rate(1)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size= 10)
    while not rospy.is_shutdown():
        pub.publish(vel)
        r.sleep()
