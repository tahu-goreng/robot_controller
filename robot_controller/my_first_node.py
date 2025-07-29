#!/usr/bin/python3
import rclpy
from rclpy.node import Node

class MyNode (Node): #inside this class is one node

    def __init__(self):
        super().__init__("first_node") #node name
        # self.get_logger().info("ROS2")
        # colcon build --symlink-install for auto update when this python code is changed
        self.counter= 0
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("hello " + str(self.counter))
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode ()
    rclpy.spin(node) #makes the code keep running until terminated by ctrl+c
    rclpy.shutdown()

if __name__ == '__main__':
    main()


# 'rqt_graph' in terminal = node graph for ROS
# 'ros2 node list' = to list all the active node
# 'ros2 node info /first_node = for node info
