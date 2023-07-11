#!/usr/bin/env python3
"""
pip3 install pySerial
pip3 install easygui
sudo apt-get install python3-tk (to install tkinter, needed for easygui)
"""
# * Note - To-Do *
# To Fix Nodes not getting destroyed correctly, we need to add argparse to get Ctrl+C and then destroy all nodes
# Python Packages
from threading import Thread
import time
import subprocess
# ROS2 Packages
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
# Streamlit Package
import streamlit as st
# from BlimpHandler import BlimpHandler
class Listener(Node):
    def __init__(self):
        super().__init__('Listener')
        self.subscription = self.create_subscription(
            Bool,
            '/Blimp1/auto',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        data_placeholder.write("Auto: {}".format(msg.data))
@st.cache_resource
def initROS():
    # To-DO
    # Everytime you reload the page, you create a new node, so we need to make sure we only have one node
    rclpy.init()
def main():
    initROS()
    global data_placeholder
    # Start the Streamlit application
    st.title("Basestation")
    data_placeholder = st.empty()
    minimal_subscriber = Listener()
    rclpy.spin(minimal_subscriber)
    # Clean up and shutdown ROS2
    # To-Do *
    # To Fix Nodes not getting destroyed correctly, we need to add argparse to get Ctrl+C and then destroy all nodes
    minimal_subscriber.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
  
