#!/usr/bin/env python3

import rospy
from first_pkg.srv import VelCommand



rospy.init_node("client", anonymous= True)


if __name__ == "__main__":
    rospy.wait_for_service("vel_commander")
    client = rospy.ServiceProxy("vel_commander", VelCommand)
    while 1 < 2:
        x = 0
        z = 0.393
        client.call(x,z)
        rospy.sleep(4)
        x = 0.3
        z = 0
        client.call(x,z)
        rospy.sleep(4)   
    
    rospy.spin()
    
