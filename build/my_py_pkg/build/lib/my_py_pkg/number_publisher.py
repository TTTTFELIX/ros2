#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberPublisherNode(Node):
    def __init__(self):
        super().__init__("number_publisher")

        self.name = "No.2 number publisher"
        self.publisher_ = self.create_publisher(Int64, "number_publish", 10)
        self.timer_ = self.create_timer(1, self.publish_number)
        self.get_logger().info(self.name + " has been started publishing number 2")


    def publish_number(self):
        msg = Int64()
        msg.data = 2
        self.publisher_.publish(msg)


def main(args = None):
    rclpy.init(args=args)
    node = NumberPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()