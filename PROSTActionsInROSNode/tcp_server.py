#!/usr/bin/env python
import rospkg
import os
import signal
import socket
from subprocess import Popen
import time
import rospy
from sensor_msgs.msg import Image
import cv2 as cv
import numpy as np
from cv_bridge import CvBridge, CvBridgeError

def start_socket(host, port):
    #import pdb;
    #pdb.set_trace()
    #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print('bind executed')
    s.listen(0)
    conn, addr = s.accept()
    print('listenning to',host,':',port)

    while not rospy.is_shutdown():
        try:
            data = conn.recv(90024)
            if '<actions>' in data:
                # print('packet received')
                print('command received:')
                print(data)
                print('')
        except Exception:
            s.close()
            print('socket closed')
    s.close()
    print('socket closed')


        #if 'TF-8"?><session-request>' in data:
         #   print('sending replay!!!')
          #  conn.sendall('<session-init><task>111</task></session-init>')
        #if data == b'killall':
            # Send the signal to all the process groups
         #   print('Received killall signal.')
            #break


if __name__ == '__main__':
 try:
     HOST = socket.gethostbyname("localhost")
     PORT = 1770
     print('HOST:',HOST)
     start_socket(HOST, PORT)
 except rospy.ROSInterruptException:
  pass