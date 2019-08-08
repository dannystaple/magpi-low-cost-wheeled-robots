import gpiozero
import time

robot = gpiozero.Robot(left=(27, 17), right=(24, 23))

try:
    # Robot actions here
    for speed in range(10, 4, -1):
        robot.value = (speed/10, speed/10)
        time.sleep(0.4)
    # Smaller turns with forward motion
    robot.value = (0.5, 1) # left
    time.sleep(1)
    robot.value = (1, 0.5) # right
    time.sleep(1)
finally:
    robot.stop()
