from signal import pause
import atexit
import gpiozero
from gpiozero import tools

robot = gpiozero.Robot(left=(27, 17), right=(24, 23))
atexit.register(robot.stop)

robot.left_motor.source = tools.sin_values()
robot.right_motor.source = tools.cos_values()

pause()

