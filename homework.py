#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist



def pose_callback(msg: Pose):

    message_1 = msg
    print(message_1.x, "\n", message_1.y, "\n\n")
    

if __name__ == "__main__":
    rospy.init_node ("turtle_controller")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size= 10)
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback= pose_callback)
    while not rospy.is_shutdown():
        cmd = Twist()
        cmd.linear.x = 1.0
        cmd.angular.z = 5.0
        pub.publish(cmd)

    rospy.spin()
