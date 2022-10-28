import rclpy
from rclpy.node import Node
from gpiozero import LED

LED_R = "22"
LED_G = "27"
LED_B = "24"

class Motors(Node):
    def __init__(self):
        super().__init__("motors")
        self.get_logger().info("Say Hello")
        led = LED(LED_R)
        led.on()



def main(args=None):
    rclpy.init(args=args)
    node = Motors()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

