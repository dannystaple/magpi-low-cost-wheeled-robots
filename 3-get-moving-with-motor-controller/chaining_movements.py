import gpiozero
import time

robot = gpiozero.Robot(left=(27, 17), right=(24, 23))

try:
    # Robot actions here
    for n in range(6):
        robot.forward()
        time.sleep(0.5)
        robot.left()
        time.sleep(0.3)
    robot.right()
    time.sleep(1)
finally:
    robot.stop()
