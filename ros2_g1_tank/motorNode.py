import rclpy
from rclpy.node import Node
import RPi.GPIO as GPIO

class Motors(Node):
    def __init__(self):
        super().__init__("motors")
        self.get_logger().info("Say Hello")
        GPIO.setmode(GPIO.BOARD)


def main(args=None):
    rclpy.init(args=args)
    node = Motors()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

