import gpiozero
import time

robot = gpiozero.Robot(left=(27, 17), right=(24, 23))

try:
    robot.forward()
    time.sleep(1)
finally:
    robot.stop()
