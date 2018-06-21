#!/usr/bin/env python

#from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Int16
from std_srvs.srv import Empty
from math import *
import rospy
import numpy

goalnr = 0

def GoalCallback(data):
    newgoalnr = data.data
    global goalnr
    print "goalnr %s" % goalnr
    if data.data != goalnr:
        rospy.wait_for_service('move_base/clear_costmaps')
        x = rospy.ServiceProxy('move_base/clear_costmaps', Empty)
        response = x()
        print "called service"
        goalnr = data.data
    print "out service"

def GoalMsg():
    rospy.init_node('CostmapFilter', anonymous=True)
    r = rospy.Rate(.1)
    rospy.Subscriber('/lidar_data', Int16, GoalCallback)
    r.sleep()


if __name__ == '__main__':
    try:
    	while not rospy.is_shutdown():
            GoalMsg()
            
            
    except rospy.ROSInterruptException: pass
    
