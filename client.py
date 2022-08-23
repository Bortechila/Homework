#!/usr/bin/env python3

import rospy
import sys
from first_pkg.srv import VelCommand

rospy.init_node("client", anonymous= True)

if __name__ == "__main__":
    
    x = float(sys.argv[1])
    z = float(sys.argv[2])

    rospy.wait_for_service("vel_commander")
    client = rospy.ServiceProxy("vel_commander", VelCommand)

    client.call(x,z)
