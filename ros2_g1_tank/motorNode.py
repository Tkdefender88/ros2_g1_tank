import rclpy
from rclpy.node import Node
from gpiozero import LED
from gpiozero import AngularServo 

LED_R = 22
LED_G = 27
LED_B = 24

servo = AngularServo(23, min_angle=0, max_angle=90)

class Motors(Node):
    def __init__(self):
        super().__init__("motors")
        self.get_logger().info("Say Hello")
        self.red = LED(LED_R)
        self.led = 0

        self.create_timer(1, self.timer_callback)
    def timer_callback(self):
        if(self.led == 1):
            self.red.on()
            self.led = 0
            self.setAngle = 0
        else:
            self.led = 1
            self.red.off()
            self.setAngle = 45

    def setAngle(angle):
        servo.angle = angle



def main(args=None):
    rclpy.init(args=args)
    node = Motors()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

